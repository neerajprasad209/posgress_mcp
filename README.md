# MCP: Gemini + PostgreSQL Integration

This project demonstrates how to integrate Google's Gemini AI models with a PostgreSQL database using the FastMCP framework. It enables natural language queries to interact with structured data, allowing for dynamic data retrieval and manipulation through conversational prompts.

---

## 📖 Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Configuration](#configuration)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [Troubleshooting](#troubleshooting)
* [Contributing](#contributing)
* [License](#license)

---

## 🧠 Overview

This application allows users to query a PostgreSQL database using natural language prompts. It leverages Google's Gemini AI models to interpret user inputs and translate them into SQL queries executed against the database. The integration is facilitated through the FastMCP framework, which manages communication between the AI model and the database.

---

## ✨ Features

* **Natural Language Querying**: Interact with your database using conversational language.
* **AI-Powered Interpretation**: Utilizes Gemini AI models to understand and process user inputs.
* **Seamless Integration**: FastMCP framework ensures smooth communication between components.
* **Customizable**: Easily adapt the system to different databases or AI models as needed.([FreeCodeCamp][1])

---

## 🛠️ Prerequisites

Before setting up the project, ensure you have the following installed:

* **Python 3.8+**: The programming language used for the application.
* **PostgreSQL**: Relational database management system.
* **pip**: Python package installer.
* **Virtual Environment Tool**: For creating isolated Python environments (e.g., `venv`).

---

## ⚙️ Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/mcp.git
   cd mcp
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv mcp_env
   ```

3. **Activate the Virtual Environment**:

   * **Windows**:

     ```bash
     mcp_env\Scripts\activate
     ```

   * **Unix or MacOS**:

     ```bash
     source mcp_env/bin/activate
     ```

4. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🧾 Configuration

1. **Set Up Environment Variables**:

   Create a `.env` file in the project root directory and add the following:

   ```env
   PG_CONN=postgresql://<username>:<password>@<host>:<port>/<database>
   GEMINI_API_KEY=your_gemini_api_key
   ```

   Replace `<username>`, `<password>`, `<host>`, `<port>`, and `<database>` with your PostgreSQL credentials and connection details. Ensure that special characters in the password are URL-encoded. For example, if your password is `redhub@432`, encode the `@` symbol as `%40`:

   ```env
   PG_CONN=postgresql://neeraj:redhub%40432@localhost:5432/mydatabase
   ```

2. **Load Environment Variables**:

   The application uses the `python-dotenv` package to load environment variables. Ensure that your `.env` file is correctly formatted and located in the project root.

---

## 🚀 Usage

1. **Start the Server**:

   The server handles communication between the Gemini model and the PostgreSQL database.

   ```bash
   python server.py
   ```

2. **Run the Client**:

   The client sends natural language prompts to the server and displays the results.

   ```bash
   python client.py
   ```

3. **Example Prompt**:

   When prompted, you can enter queries like:

   ```
   Get the number of users per country in the users table.
   ```



The system will process this input, translate it into an SQL query, execute it against the PostgreSQL database, and return the results.

---

## 🗂️ Project Structure

```

mcp/
├── client.py
├── server.py
├── .env
├── requirements.txt
├── mcp_env/
└── README.md
```



* **client.py**: Handles user input and displays results.
* **server.py**: Manages interactions between the AI model and the database.
* **.env**: Stores environment variables for configuration.
* **requirements.txt**: Lists Python dependencies.
* **mcp\_env/**: Virtual environment directory.
* **README.md**: Project documentation.([Gist][2])

---

## 🐞 Troubleshooting

* **ModuleNotFoundError: No module named 'psycopg2'**:

  Ensure that all dependencies are installed:

  ```bash
  pip install -r requirements.txt
  ```

* **AttributeError: 'FastMCP' object has no attribute 'run\_stdio'**:

  Verify that you're using the correct method to start the server. The `FastMCP` class may not have a `run_stdio` method. Ensure that your `server.py` script is correctly implemented.

* **ValidationError: env.PG\_CONN Input should be a valid string**:

  Check that the `PG_CONN` variable is correctly set in your `.env` file and that the file is properly formatted.

* **ClientError: 404 NOT\_FOUND for model 'gemini-2.5-pro'**:

  The specified model may not be available or supported. Use the `ListModels` method to retrieve available models and update your code accordingly.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---