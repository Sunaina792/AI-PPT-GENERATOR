# AI PowerPoint Generator

An AI-powered PowerPoint presentation generator that uses Google's Gemini API to create engaging presentations on any topic with automatic image integration.

## Features

- 🤖 AI-generated comprehensive content using Google Gemini
- 🎨 Professional slide layouts with automatic formatting
- 🖼️ Smart image integration with automatic fallback (Pixabay → Pexels → Placeholder)
- 📊 Multiple slide types (title, introduction, concepts, applications, advantages)
- 🔄 Robust fallback mechanisms for reliability
- 🎯 Customizable slide count and topics
- 📈 Structured content flow with logical progression
- 🎯 Detailed explanations and professional formatting
- 📐 Fixed text alignment issues in image slides


## Demo PPT

Here’s a sample PowerPoint generated with this tool:

[📂 Download Demo PPT](Machine_Learning_Fundamentals_presentation.pptx)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd AI_PPT_generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_gemini_api_key_here
PIXABAY_API_KEY=your_pixabay_api_key_here
# OR
PEXELS_API_KEY=your_pexels_api_key_here
```

## Usage

### 🌐 Web Interface (Recommended)

Launch the Streamlit web application for an easy-to-use interface:

```bash
# Option 1: Use the launcher script (recommended)
python run_app.py

# Option 2: Platform-specific launchers
# Windows:
launch_app.bat

# Unix/Linux/Mac:
./launch_app.sh

# Option 3: Direct Streamlit command
streamlit run app.py
```

The web app provides:
- 🎨 Beautiful, intuitive interface
- 📝 Topic suggestions and custom input
- ⚙️ Advanced configuration options
- 📊 Real-time progress tracking
- 📥 Direct download of presentations
- 🔄 Automatic API fallback visualization

### 💻 Command Line Usage

```python
from main import PPTGenerator

# Initialize the generator with automatic fallback (Pixabay → Pexels → Placeholder)
generator = PPTGenerator(image_api="pixabay")

# Generate a comprehensive presentation
topic = "Artificial Intelligence in Healthcare"
num_slides = 6
output_file = generator.generate_presentation(topic, num_slides, "my_presentation.pptx")
```

### Using Pexels for Images

```python
# Initialize the generator with Pexels
generator = PPTGenerator(image_api="pexels")

# Generate presentation
output_file = generator.generate_presentation(
    topic="Machine Learning Basics",
    num_slides=8,
    output_path="ml_presentation.pptx"
)
```

### Testing the Generator

```bash
# Test the automatic fallback system
python quick_test.py

# Comprehensive testing
python test_fallback.py

# Generate sample presentations
python test_generator.py
```

## Configuration

### Required API Keys

1. **Gemini API Key**: Get from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. **Pixabay API Key**: Get from [Pixabay API](https://pixabay.com/api/docs/) (optional, for images)
3. **Pexels API Key**: Get from [Pexels API](https://www.pexels.com/api/) (optional, for images)

### Environment Variables

- `GEMINI_API_KEY`: Your Google Gemini API key (required)
- `PIXABAY_API_KEY`: Your Pixabay API key (optional)
- `PEXELS_API_KEY`: Your Pexels API key (optional)

## Project Structure

```
AI_PPT_generator/
├── main.py                 # Main generator class
├── app.py                  # Streamlit web application
├── run_app.py             # App launcher script
├── requirements.txt        # Python dependencies
├── pyproject.toml         # Project configuration
├── README.md              # This file
├── config.example         # Configuration template
├── test_generator.py      # Test script
├── quick_test.py          # Quick API test script
├── test_fallback.py       # Fallback testing script
├── setup.py               # Setup helper script
└── .env                   # Environment variables (create this)
```

## Content Structure

The generator creates comprehensive presentations with the following structure:

1. **Title Slide**: Introduction and overview
2. **Overview/Introduction**: Definition and background
3. **Key Concepts**: Fundamental principles and theories
4. **Applications**: Real-world use cases and examples
5. **Advantages**: Benefits and positive aspects

## API Dependencies

- **Google Gemini**: Comprehensive content generation and intelligent image descriptions
- **Pixabay**: High-quality stock image search (5000 requests/hour free)
- **Pexels**: Professional stock photos (free tier available)
- **python-pptx**: Professional PowerPoint file creation and manipulation

## Error Handling

The generator includes robust error handling:
- Fallback content when AI generation fails
- **Automatic image API fallback**: Pixabay → Pexels → Placeholder
- Graceful degradation for missing API keys
- Automatic cleanup of temporary files
- Detailed error logging and debugging output

## Automatic Image API Fallback

The generator now includes intelligent automatic fallback for image APIs:
- **Primary**: Pixabay API (5000 requests/hour free)
- **Fallback**: Pexels API (free tier available)
- **Final Fallback**: Custom placeholder images

This ensures your presentations always have images, even if one API is down or has no results.

## Text Alignment Fixes

The latest version includes fixes for text alignment issues in slides with images:
- Proper text positioning on the left side
- Images positioned on the right side
- Consistent spacing and formatting
- Better content flow and readability

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure your `.env` file is properly configured
2. **Image Download Failures**: Check your Pixabay/Pexels API key or internet connection
3. **Content Generation Issues**: Verify your Gemini API key and quota

### Support

For issues and questions, please open an issue on the repository.
