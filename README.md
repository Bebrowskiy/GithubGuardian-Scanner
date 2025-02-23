# GitGuardian-Scanner

**GitGuardian-Scanner** is a tool designed to scan public GitHub repositories for sensitive data, including API tokens, private keys, and other secrets that may have been accidentally committed. By scanning commit history and repository files, this tool helps you ensure that your codebase remains secure and free of exposed credentials.

## Features

- Scans the entire GitHub repository, including all commits and files.
- Identifies and highlights sensitive information like API tokens, private keys, and credentials.
- Provides clear results to help developers clean up and secure their repositories.
- Open-source, easy to use, and highly configurable.

## Installation

You can easily install and run GitGuardian-Scanner on your local machine using the following steps:

### Installation Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/Bebrowskiy/GitGuardian-Scanner.git
    ```

2. Navigate to the project directory:
    ```bash
    cd GitGuardian-Scanner
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. (Optional) If you're planning to contribute or modify the tool, consider setting up a virtual environment.

## Usage

Once installed, you can run GitGuardian-Scanner to start scanning a repository for exposed tokens. Here's how:

### Basic Command

To scan a repository, run:

```bash
python scanner.py