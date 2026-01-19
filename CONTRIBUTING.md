# Contributing to Lies as a Service

Thanks for your interest in contributing! 🎉

## How to Contribute

### Adding New Lies

1. Fork the repository
2. Edit `responses.py`
3. Add your lies to the appropriate category
4. Make sure they're:
   - Humorous and obviously fake
   - Not offensive or inappropriate
   - Workplace or everyday life related
5. Submit a pull request

### Creating New Categories

1. Add a new category to the `LIES` dictionary in `responses.py`
2. Add at least 10 lies to the new category
3. Update the README.md with the new category description
4. Submit a pull request

### Code Contributions

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test locally with `python main.py`
5. Test with Docker: `docker-compose up --build`
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a pull request

## Code Style

- Follow PEP 8 for Python code
- Keep lies concise and punchy
- Add comments for complex logic
- Update documentation when needed

## Testing

Before submitting:
- Test the API locally
- Verify Docker build works
- Check all endpoints return valid JSON
- Ensure rate limiting works

## Questions?

Open an issue and we'll help you out!
