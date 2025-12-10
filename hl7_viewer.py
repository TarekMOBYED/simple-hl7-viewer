# hl7_viewer.py

import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from hl7_parser import load_hl7_from_file, split_segments, parse_segment


class HL7ViewerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Simple HL7 Viewer")
        self.geometry("900x500")

        self.segments = []
        self.parsed_segments = []

        self._build_ui()

    def _build_ui(self):
        top_frame = ttk.Frame(self)
        top_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        load_btn = ttk.Button(top_frame, text="Load HL7 File", command=self.load_hl7_file)
        load_btn.pack(side=tk.LEFT)

        self.search_var = tk.StringVar()

        search_label = ttk.Label(top_frame, text="Search:")
        search_label.pack(side=tk.LEFT, padx=(10, 2))

        search_entry = ttk.Entry(top_frame, textvariable=self.search_var, width=30)
        search_entry.pack(side=tk.LEFT)

        search_btn = ttk.Button(top_frame, text="Find", command=self.search_hl7)
        search_btn.pack(side=tk.LEFT, padx=5)

        search_entry.bind("<Return>", lambda event: self.search_hl7())

        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.Y)

        lbl_segments = ttk.Label(left_frame, text="Segments")
        lbl_segments.pack(anchor="w")

        self.segment_listbox = tk.Listbox(left_frame, width=25)
        self.segment_listbox.pack(fill=tk.Y, expand=False)
        self.segment_listbox.bind("<<ListboxSelect>>", self.on_segment_select)

        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))

        self.selected_segment_label = ttk.Label(
            right_frame,
            text="Segment: -",
            font=("TkDefaultFont", 10, "bold")
        )
        self.selected_segment_label.pack(anchor="w")

        columns = ("field_no", "value")
        self.fields_tree = ttk.Treeview(right_frame, columns=columns, show="headings")
        self.fields_tree.heading("field_no", text="Field #")
        self.fields_tree.heading("value", text="Value")

        self.fields_tree.column("field_no", width=70, anchor="center")
        self.fields_tree.column("value", width=600, anchor="w")

        self.fields_tree.pack(fill=tk.BOTH, expand=True, pady=5)

        patient_frame = ttk.LabelFrame(right_frame, text="Patient Information")
        patient_frame.pack(fill=tk.X, pady=10)

        self.lbl_pid = ttk.Label(patient_frame, text="Patient ID: -")
        self.lbl_pid.pack(anchor="w")

        self.lbl_name = ttk.Label(patient_frame, text="Name: -")
        self.lbl_name.pack(anchor="w")

        self.lbl_dob = ttk.Label(patient_frame, text="DOB: -")
        self.lbl_dob.pack(anchor="w")

        self.lbl_gender = ttk.Label(patient_frame, text="Gender: -")
        self.lbl_gender.pack(anchor="w")

        self.lbl_address = ttk.Label(patient_frame, text="Address: -")
        self.lbl_address.pack(anchor="w")

    def load_hl7_file(self):
        file_path = filedialog.askopenfilename(
            title="Select HL7 File",
            filetypes=[("HL7 files", "*.hl7;*.txt"), ("All files", "*.*")]
        )
        if not file_path:
            return

        try:
            text = load_hl7_from_file(file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Error loading file:\n{e}")
            return

        self.segments = split_segments(text)
        self.parsed_segments = [parse_segment(seg) for seg in self.segments]

        self.segment_listbox.delete(0, tk.END)
        for seg_name, fields in self.parsed_segments:
            self.segment_listbox.insert(tk.END, seg_name)

        self.clear_fields()
        self.selected_segment_label.config(text="Segment: -")

        self.extract_patient_info()

    def on_segment_select(self, event):
        selection = self.segment_listbox.curselection()
        if not selection:
            return

        index = selection[0]
        seg_name, fields = self.parsed_segments[index]

        self.selected_segment_label.config(text=f"Segment: {seg_name}")

        self.clear_fields()
        for i, value in enumerate(fields, start=1):
            self.fields_tree.insert("", tk.END, values=(i, value))

    def clear_fields(self):
        for item in self.fields_tree.get_children():
            self.fields_tree.delete(item)

    def extract_patient_info(self):
        for seg_name, fields in self.parsed_segments:
            if seg_name == "PID":
                patient_id = fields[2] if len(fields) > 2 else "-"
                name = fields[4] if len(fields) > 4 else "-"
                dob = fields[6] if len(fields) > 6 else "-"
                gender = fields[7] if len(fields) > 7 else "-"
                address = fields[10] if len(fields) > 10 else "-"

                if "^" in name:
                    parts = name.split("^")
                    if len(parts) > 1:
                        name = f"{parts[1]} {parts[0]}"

                self.lbl_pid.config(text=f"Patient ID: {patient_id}")
                self.lbl_name.config(text=f"Name: {name}")
                self.lbl_dob.config(text=f"DOB: {dob}")
                self.lbl_gender.config(text=f"Gender: {gender}")
                self.lbl_address.config(text=f"Address: {address}")
                return

        self.lbl_pid.config(text="Patient ID: -")
        self.lbl_name.config(text="Name: -")
        self.lbl_dob.config(text="DOB: -")
        self.lbl_gender.config(text="Gender: -")
        self.lbl_address.config(text="Address: -")

    def search_hl7(self):
        term = self.search_var.get().strip()
        if not term:
            messagebox.showwarning("Search", "Enter search term.")
            return

        if not self.parsed_segments:
            messagebox.showwarning("Search", "No HL7 data loaded.")
            return

        term_lower = term.lower()

        for idx, (seg_name, fields) in enumerate(self.parsed_segments):
            full_text = seg_name + "|" + "|".join(fields)
            if term_lower in full_text.lower():
                self.segment_listbox.selection_clear(0, tk.END)
                self.segment_listbox.selection_set(idx)
                self.segment_listbox.activate(idx)
                self.segment_listbox.see(idx)
                self.on_segment_select(None)
                return

        messagebox.showinfo("Search", f"No match found for: {term}")


if __name__ == "__main__":
    app = HL7ViewerApp()
    app.mainloop()
