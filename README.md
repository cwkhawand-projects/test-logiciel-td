# Module Test Logiciel

Welcome to the **Project Title** repository! Thank you for contributing to this project. Follow the guidelines below to set up the project and collaborate effectively.

## Getting Started

To contribute to this project, please follow these steps:

### 1. Clone the Repository
First, clone the repository to your local machine using the following command:

```bash
git clone https://github.com/cwkhawand/test-logiciel.git
cd test-logiciel
```

### 2. Create a New Branch
Always work on a separate branch for your feature or fix. Use the following command to create and switch to a new branch:

```bash
git checkout -b your-branch-name
```

Branch names should be descriptive, e.g., `feature/login-page`, `bugfix/header-alignment`.

### 3. Develop and Test
- Make your changes.
- Ensure that all tests pass before pushing your changes. Run the tests with:

```bash
python3 -m unittest discover -s ./tests  -p 'test_*.py'
```

### 4. Push Your Changes
Once all tests pass, push your branch to the remote repository:

```bash
git add .
git commit -m "Your descriptive commit message"
git push origin your-branch-name
```

### 5. Open a Pull Request
After pushing your branch:
1. Go to the [GitHub repository](https://github.com/cwkhawand/test-logiciel).
2. Click on **Pull Requests**.
3. Open a new Pull Request (PR) to merge your branch into the `main` branch.
4. Add a meaningful title and description to your PR.

### 6. Review and Merge
- Your PR will be reviewed by other contributors or maintainers.
- Once approved, it will be merged into the `main` branch.

---

## Guidelines

- Ensure your code follows the project's coding standards.
- Keep your commits clean and descriptive.
- Always test your changes locally before submitting a PR.
- Avoid making changes directly to the `main` branch.
- Prepend `test_` to test file names (e.g. test_helloworld.py)

---

## Need Help?
If you run into any issues, feel free to create an [issue](https://github.com/cwkhawand/test-logiciel/issues) or reach out to the maintainers.

Happy Coding! 🚀
