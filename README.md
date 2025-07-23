# 🔌 IoT-Aware Script Compiler for Home Automation

This project is a **DSL-based script compiler** designed to simulate smart home automation. It allows users to write simple rule-based scripts using a custom domain-specific language (DSL), which are then compiled into executable Python code. This simulation mimics how smart devices like lights, fans, and sensors behave based on real-world triggers.

---

## 📜 Features

- ✅ Simple rule-based language for home automation logic
- ✅ Compiles DSL into executable Python code
- ✅ Simulates real-time smart home scenarios
- ✅ Easily extensible for more rules and devices
- ✅ Helps prototype IoT automation logic without hardware

---

## 🧠 How It Works

1. You write automation rules in a `.dsl` script using intuitive commands.
2. The compiler parses your script, converts it into Python code.
3. That Python code simulates the devices’ behavior based on the conditions.

---

## 📁 Folder Structure

IOTAwareScriptCompiler/
├── compiler.py # Core compilation logic
├── executor.py # Executes compiled automation logic
├── main.py # Entry point for running compiler
├── sample.dsl # Example DSL rules
├── requirements.txt # Python dependencies
├── gui.py # (Optional) GUI to interact with the compiler
├── voice_recognition.py # (Optional) Voice-based input
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/Deepans2004/IOTAwareScriptCompiler.git
cd IOTAwareScriptCompiler
2. Install Dependencies

pip install -r requirements.txt
3. Write Automation Rules
Open or create a file like sample.dsl:


TURN ON light IF motion_detected
TURN OFF fan IF temperature_low
4. Run the Compiler

python gui.py
