# Contributing to Sample Distributor

First, thank you for considering contributing to this project! 🎉

## How to Contribute

### Reporting Bugs

Before reporting a bug, check if it hasn't been reported already. If not, create an issue including:

- **Clear description** of the problem
- **Steps to reproduce** the bug
- **Expected behavior** vs **actual behavior**
- **Environment** (Python version, operating system)
- **Example code** that demonstrates the problem

### Suggesting Enhancements

To suggest a new feature:

1. Open an issue with the "enhancement" tag
2. Explain **why** this feature would be useful
3. Describe **how** it should work
4. If possible, suggest an implementation

### Development Process

1. **Fork** the repository
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/your-username/sample-distributor.git
   cd sample-distributor
   ```

3. **Create a branch** for your feature:
   ```bash
   git checkout -b feature/feature-name
   ```

4. **Make your changes** following the code guidelines

5. **Test** your changes:
   ```bash
   python sample_distributor.py
   ```

6. **Commit** your changes:
   ```bash
   git commit -m "Add: clear description of the change"
   ```

7. **Push** to your branch:
   ```bash
   git push origin feature/feature-name
   ```

8. **Open a Pull Request**

## Code Guidelines

### Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python style
- Use descriptive names for variables and functions
- Add comments for complex code
- Keep functions small and focused on a single task

### Well-Formatted Code Example

```python
def dividir_amostras(amostras, num_grupos):
    """
    Divide a list of samples into groups randomly.
    
    Args:
        amostras (list): List of samples to be divided
        num_grupos (int): Number of groups to be created
    
    Returns:
        list: List of groups with distributed samples
    """
    random.shuffle(amostras)
    grupos = [sorted(amostras[i::num_grupos]) for i in range(num_grupos)]
    return grupos
```

### Commit Structure

Use clear commit messages:

- `Add: new feature`
- `Fix: bug correction`
- `Update: improvement of existing feature`
- `Docs: documentation update`
- `Style: formatting changes`
- `Refactor: code refactoring`

## Types of Contributions

### 🐛 Bug Fixes
- Identify and fix code issues
- Improve error handling
- Fix edge cases

### ✨ New Features
Some feature ideas:
- Export results to CSV/Excel
- GUI with tkinter
- Save and load configurations
- Support for more than 4 stages
- Graphical visualization of groups
- More robust input validation

### 📚 Documentation
- Improve README.md
- Add docstrings to functions
- Create tutorials or examples
- Translate documentation

### 🧪 Testing
- Create unit tests
- Integration tests
- Performance tests

## Development Environment Setup

### Requirements
- Python 3.6+
- Git

### Optional Setup
For more advanced development:

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install development tools (optional)
pip install black flake8 pytest
```

## Review Process

### What we check:
- ✅ Code works correctly
- ✅ Follows style guidelines
- ✅ Doesn't break existing functionality
- ✅ Includes adequate documentation
- ✅ Commit messages are clear

### Response time:
- Issues: Response in 2-3 days
- Pull Requests: Review in 3-5 days

## Code of Conduct

### Our Commitment

We are committed to making this project a harassment-free experience for everyone, regardless of:
- Age, body size, disability, ethnicity, gender
- Experience level, nationality, race, religion
- Gender identity and expression, sexual orientation

### Expected Behaviors

- Use welcoming and inclusive language
- Respect different viewpoints
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards other members

### Unacceptable Behaviors

- Sexual language or imagery
- Trolling comments, insults or personal attacks
- Public or private harassment
- Publishing private information without permission

## Questions?

If you have questions about how to contribute:
- Open an issue with the "question" tag
- Contact through project channels

**Thank you for contributing! 🚀**
