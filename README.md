# Simple HL7 Viewer (Python, Tkinter)

This project provides a clean and lightweight graphical viewer for HL7 v2.x messages.  
It enables loading, parsing, and inspecting message segments in a structured way.  
The tool is developed in Python using Tkinter and is intended for educational and medical informatics environments.

---

## Features

- Load HL7 files (.hl7 or .txt)
- Segment detection and listing (MSH, PID, PV1, etc.)
- Table-based display of segment fields
- Patient Information Panel based on the PID segment:
  - Patient ID  
  - Name  
  - Date of Birth  
  - Gender  
  - Address  
- Text search within the message
- Simple and organized Tkinter interface

---

## Screenshot

 ![Simple HL7 Viewer](assets/SIMPLE_HL7_VIEWER.png)
---

## Project Structure

```
simple-hl7-viewer/
│
├── hl7_viewer.py
├── hl7_parser.py
├── sample_data/
│   └── sample_adt.hl7
├── assets/
│   └── SIMPLE_HL7_VIEWER_.png
└── README.md
```


---

## How to Run

Ensure Python 3 is installed on the system.

python3 hl7_viewer.py

Tkinter is included in standard Python installations.

---

## Example HL7 Message

A sample ADT^A01 message is included:

MSH|^~&|HIS|HOSPITAL|RIS|RAD|20250101120000||ADT^A01|123456|P|2.3
PID|1||P12345^^^HOSPITAL||MUSTERMANN^ERIKA||19900101|F|||MUSTERSTRASSE 1^^DORTMUND^^44137^DE
PV1|1|I|STATION^ROOM1^BED1||||1234^ARZT^MAX|||||||||||V123456

---

## Learning Outcomes

- Understanding HL7 v2.x structure  
- Parsing HL7 messages programmatically  
- Extracting patient-related data  
- Designing GUI applications with Tkinter  
- Structuring and documenting small software tools  

---

## Use Cases

- Medical informatics coursework  
- HL7 message exploration  
- Teaching and demonstration  
- Basic inspection of HL7 message structure  

---

## License

This project is released under the MIT License.

