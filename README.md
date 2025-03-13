
# TestGenie 📜✨

**TestGenie** is a powerful VS Code extension designed to automate the process of generating test cases. It works seamlessly with your code and API/Swagger contracts. With a backend built using FastAPI and Gemini Client, TestGenie not only generates high-quality test cases, but also helps improve your Swagger contracts, ensuring they meet the best practices and get higher scores in contract testing tools like [42Crunch](https://42crunch.com/). 🚀

## Features 🛠️

- **Test Case Generation**: 
  - Automatically generates test cases directly from your code.
  - Generates test cases from your API/Swagger contracts for easy integration testing.
  
- **Swagger Contract Improvement**: 
  - Enhance your Swagger contract to improve its score on contract testing platforms like 42Crunch.
  
- **FastAPI Backend**: 
  - Robust backend built with FastAPI, allowing seamless interactions between the VS Code extension and your project.

- **Gemini Client Integration**: 
  - Leverages Gemini Client to communicate efficiently with the backend for swift generation of test cases and contract improvements.

## 🛠️ Installation

### Prerequisites

- **Node.js** and **npm** (for VS Code Extension)
- **Python** (for FastAPI Backend)
- **VS Code** (obviously!) 😄

### Step 1: Install the VS Code Extension

1. Open VS Code.
2. Go to the Extensions tab on the left side of the screen.
3. Search for **TestGenie** and click **Install**.

Alternatively, you can download the `.vsix` file and install it manually via the command palette with `Extensions: Install from VSIX`.

### Step 2: Set up the Backend

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/TestGenie.git
   cd TestGenie/backend
   ```

2. Install required Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI backend:

   ```bash
   uvicorn main:app --reload
   ```

4. Ensure the backend is running on `http://localhost:8000`.

### Step 3: Configuration (Optional)

TestGenie can be configured for specific behaviors, like test case generation settings and Swagger contract improvements. Check the `config.json` in the extension’s settings or modify the FastAPI backend to meet your needs.

## 📝 Usage

1. **Generate Test Cases from Code**:
   - Open a JavaScript/TypeScript file in VS Code.
   - Use the `TestGenie: Generate Test Cases` command from the Command Palette.
   - Test cases will be automatically generated and inserted into your project!

2. **Generate Test Cases from Swagger Contract**:
   - Open your Swagger contract (either locally or via an API endpoint).
   - Use the `TestGenie: Generate Test Cases from Swagger` command.
   - TestGenie will parse the contract and generate relevant test cases for you.

3. **Improve Swagger Contract**:
   - Use the `TestGenie: Improve Swagger Contract` command.
   - TestGenie will analyze your Swagger contract and suggest improvements to make it more robust, ensuring a better score on tools like 42Crunch.

## 💡 Why Use TestGenie?

- **Automation**: Save time by automating the generation of test cases.
- **Boost Test Quality**: Generate comprehensive test cases directly from code and API contracts, making sure you don't miss edge cases.
- **Improve API Contracts**: With built-in contract improvement features, your Swagger API contracts will always be top-notch.
- **Seamless Integration**: Easily integrates into your existing development workflow in VS Code.

## ⚡ Contributing

We welcome contributions to TestGenie! If you'd like to help improve the project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to your branch (`git push origin feature/your-feature-name`).
5. Open a pull request with a clear description of your changes.

---

Feel free to adjust the URLs, installation steps, and any other project-specific details as necessary!
