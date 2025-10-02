# Contributing to Hactoberfest 2025 Programming Solutions

First off, thank you for considering contributing to this repository! 🎉 Your contributions help make this a better resource for learning programming and algorithms.

## 🌟 How to Contribute

There are many ways you can contribute to this project:

### 🐛 Bug Fixes
- Fix logical errors in existing solutions
- Correct syntax issues
- Resolve runtime errors

### ⚡ Performance Improvements
- Optimize algorithms for better time complexity
- Reduce space complexity where possible
- Implement more efficient data structures

### 📝 Documentation
- Add or improve code comments
- Create explanatory documentation for complex algorithms
- Add time and space complexity analysis

### ✅ Testing
- Add test cases for existing solutions
- Create automated testing scripts
- Validate edge cases

### 🆕 New Solutions
- Add alternative approaches to existing problems
- Implement solutions in different programming languages
- Add new practice problems with solutions

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have:
- Python 3.6 or higher installed
- Git installed on your local machine
- A GitHub account
- Basic knowledge of data structures and algorithms

### Setting Up Your Development Environment

1. **Fork the Repository**
   - Click the "Fork" button at the top right of this repository
   - This creates a copy of the repository in your GitHub account

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/hactoberfest25.git
   cd hactoberfest25
   ```

3. **Create a New Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```

4. **Set Up Upstream Remote**
   ```bash
   git remote add upstream https://github.com/24f2003068/hactoberfest25.git
   ```

## 📋 Contribution Guidelines

### Code Style

#### Python Code
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Include type hints where appropriate

```python
def calculate_fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number using dynamic programming.
    
    Args:
        n (int): The position in the Fibonacci sequence
        
    Returns:
        int: The nth Fibonacci number
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b
```

#### SQL Code
- Use uppercase for SQL keywords
- Proper indentation for complex queries
- Clear table and column aliases

```sql
SELECT 
    u.username,
    COUNT(p.post_id) AS total_posts
FROM users u
LEFT JOIN posts p ON u.user_id = p.user_id
WHERE u.created_date >= '2025-01-01'
GROUP BY u.user_id, u.username
ORDER BY total_posts DESC;
```

### Commit Messages

Write clear, descriptive commit messages:

```bash
# Good examples:
git commit -m "Fix: Correct logic error in Goldbach's conjecture implementation"
git commit -m "Add: Binary search solution with O(log n) complexity"
git commit -m "Optimize: Improve merge sort performance by 20%"
git commit -m "Docs: Add complexity analysis for heap operations"

# Bad examples:
git commit -m "fix bug"
git commit -m "update code"
git commit -m "changes"
```

### File Organization

- Place files in appropriate week folders
- Use descriptive filenames
- Include problem descriptions as comments at the top of files
- Group related functions together

### Testing Your Changes

Before submitting your contribution:

1. **Test Your Code**
   ```bash
   python your_solution.py
   ```

2. **Check for Syntax Errors**
   ```bash
   python -m py_compile your_solution.py
   ```

3. **Verify Edge Cases**
   - Empty inputs
   - Large inputs
   - Boundary conditions

## 📝 Pull Request Process

### Before Submitting

1. **Update Your Fork**
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   git push origin main
   ```

2. **Rebase Your Feature Branch**
   ```bash
   git checkout your-feature-branch
   git rebase main
   ```

3. **Run Final Tests**
   - Ensure all solutions work correctly
   - Check that new code follows style guidelines
   - Verify documentation is complete

### Creating the Pull Request

1. **Push Your Changes**
   ```bash
   git push origin your-feature-branch
   ```

2. **Create Pull Request**
   - Go to your fork on GitHub
   - Click "New pull request"
   - Choose your feature branch
   - Fill out the PR template

### Pull Request Template

When creating a pull request, please include:

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Performance improvement
- [ ] Documentation update
- [ ] Code refactoring

## Testing
- [ ] Tested with sample inputs
- [ ] Verified edge cases
- [ ] No syntax errors

## Files Changed
- `path/to/file1.py` - Brief description of changes
- `path/to/file2.py` - Brief description of changes

## Additional Notes
Any additional information or context.
```

## 🎯 Issue Guidelines

### Creating Issues

When creating an issue:

1. **Use descriptive titles**
   - Good: "Merge sort implementation has incorrect time complexity"
   - Bad: "Fix bug"

2. **Provide context**
   - What were you trying to do?
   - What happened instead?
   - Steps to reproduce the issue

3. **Label appropriately**
   - `bug` for errors
   - `enhancement` for new features
   - `documentation` for doc improvements
   - `good first issue` for beginner-friendly tasks

### Working on Issues

- Comment on issues you'd like to work on
- Wait for assignment before starting work
- Ask questions if anything is unclear

## 🏆 Hacktoberfest Guidelines

If you're contributing for Hacktoberfest:

1. **Quality over Quantity**
   - Focus on meaningful contributions
   - Avoid trivial changes like fixing typos in comments

2. **Follow Hacktoberfest Rules**
   - PRs must be submitted between October 1-31
   - PRs must be to public repositories
   - PRs must be meaningful contributions

3. **Hacktoberfest Labels**
   - Look for issues labeled `hacktoberfest`
   - Consider `good first issue` for beginners

## 🤝 Community Standards

### Code of Conduct

- Be respectful and inclusive
- Help newcomers learn
- Provide constructive feedback
- Focus on what is best for the community

### Getting Help

- **Documentation**: Check existing code comments and README
- **Issues**: Create an issue for questions
- **Discussions**: Use GitHub discussions for general questions

## 🎓 Learning Resources

### Algorithm Resources
- [GeeksforGeeks](https://www.geeksforgeeks.org/)
- [LeetCode](https://leetcode.com/)
- [HackerRank](https://www.hackerrank.com/)

### Python Resources
- [Python.org Documentation](https://docs.python.org/3/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)

### SQL Resources
- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)
- [SQLBolt](https://sqlbolt.com/)

## 📞 Contact

If you have questions or need help:

- Open an issue for technical questions
- Use GitHub discussions for general questions
- Review existing issues and PRs for context

## 🙏 Recognition

Contributors will be acknowledged in:
- Repository contributors list
- Release notes for significant contributions
- Special recognition for high-quality contributions

Thank you for contributing to the Hactoberfest 2025 Programming Solutions repository! 🚀

---

Happy coding! 💻✨