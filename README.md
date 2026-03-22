DevOps Multi-Language CI Project

This project tests the same simple calculator logic across C++, Python, and TypeScript, with a CI pipeline set up using GitHub Actions.

The goal was to understand how testing and CI behave across different languages and ecosystems, not just in isolation.

---

What this project shows

- Running tests across multiple languages in one repo
- Setting up CI pipelines using GitHub Actions
- Handling different testing tools (PyTest, Jest, C++ asserts)
- Structuring a repo in a way that scales

---

Project Structure

devops-prep/
├── cpp/                 # C++ code + tests
├── python/              # Python code + pytest
├── typescript/          # TypeScript code + Jest
├── .github/workflows/   # CI setup
└── README.md

---

CI Pipeline

The pipeline runs tests for each language and makes sure everything stays consistent.

Each part can fail independently, which makes debugging easier and reflects how real systems behave when different services are involved.

---

Run locally

Python

cd python
pip install -r requirements.txt
pytest

C++

cd cpp
g++ calculator.cpp test_calculator.cpp -o test
./test

TypeScript

cd typescript
npm install
npm test

---

Why multiple languages?

In real-world systems, different parts are often written in different languages.

This project is a small way to simulate that and understand:

- how testing differs across ecosystems
- how CI handles multiple environments
- how to keep behavior consistent across implementations
