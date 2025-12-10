# Simple HL7 Viewer (Python)

A compact tool for loading and inspecting HL7 v2.x messages.  
The application provides a clear view of message structure and segment content, making it suitable for educational use, training in medical informatics, and basic integration testing.

The viewer is implemented in Python using Tkinter.

---

## Features

- Load HL7 files (.hl7 or .txt)
- Segment detection (MSH, PID, PV1, etc.)
- Field-by-field visualization within each segment
- Patient information extraction from PID, including:
  - Patient ID  
  - Name  
  - Date of Birth  
  - Gender  
  - Address  
- Search function for locating terms within the message
- Clean and minimal interface

---

## Screenshot

![Simple HL7 Viewer](assets/SIMPLE_HL7_VIEWER_.png)

---

## Project Structure

simple-hl7-viewer/
├── assets/
│ └── SIMPLE_HL7_VIEWER_.png
├── sample_data/
│ └── sample_adt.hl7
├── hl7_viewer.py
├── hl7_parser.py
└── README.md

---

## Running the Application

Python 3 is required.

Start the viewer with:

python3 hl7_viewer.py

Tkinter is included in standard Python installations.

---

## Example HL7 Message

An ADT^A01 sample is included:

MSH|^~&|HIS|HOSPITAL|RIS|RAD|20250101120000||ADT^A01|123456|P|2.3
PID|1||P12345^^^HOSPITAL||MUSTERMANN^ERIKA||19900101|F|||MUSTERSTRASSE 1^^DORTMUND^^44137^DE
PV1|1|I|STATION^ROOM1^BED1||||1234^ARZT^MAX|||||||||||V123456

---

## Learning Outcomes

- Understanding HL7 v2.x message structure  
- Parsing and analyzing HL7 messages programmatically  
- Extracting key patient-related fields  
- Building small graphical tools in Python  
- Structuring and documenting technical projects

---

## Use Cases

- Medical informatics coursework  
- HL7 training and demonstrations  
- Basic message inspection during integration exercises  

---

## License

This project is released under the MIT License.
