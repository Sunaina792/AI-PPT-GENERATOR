import streamlit as st
import os
import sys
from pathlib import Path
import time
from datetime import datetime
import tempfile

# Add the current directory to the path to import your modules
sys.path.append(str(Path(__file__).parent))

# Import your existing generator classes
try:
    from NEW import PPTGenerator
except ImportError:
    st.error("⚠️ Could not import PPTGenerator module. Make sure main.py is in the same directory.")
    st.stop()

# Page configuration
st.set_page_config(
    page_title="AI PowerPoint Generator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .api-status {
        padding: 0.5rem;
        border-radius: 5px;
        margin: 0.2rem 0;
    }
    .api-available {
        background-color: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
    }
    .api-unavailable {
        background-color: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
    }
    .feature-box {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        margin: 0.5rem 0;
    }
    .success-box {
        background-color: #d1ecf1;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #17a2b8;
        margin: 0.5rem 0;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #ffc107;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

def check_api_availability():
    """Check which APIs are available based on environment variables"""
    content_apis = {}
    image_apis = {}

    # Content APIs
    content_apis['gemini'] = bool(os.getenv('GEMINI_API_KEY'))

    # Image APIs
    
    image_apis['pexels'] = bool(os.getenv('PEXELS_API_KEY'))
    image_apis['pixabay'] = bool(os.getenv('PIXABAY_API_KEY'))

    return content_apis, image_apis

def display_api_status(content_apis, image_apis):
    """Display API availability status"""
    st.sidebar.markdown("### 🔌 API Status")

    st.sidebar.markdown("**Content Generation APIs:**")
    for api, available in content_apis.items():
        status_class = "api-available" if available else "api-unavailable"
        status_text = "✅ Available" if available else "❌ Not configured"
        st.sidebar.markdown(
            f'<div class="api-status {status_class}">{api.title()}: {status_text}</div>',
            unsafe_allow_html=True
        )

    st.sidebar.markdown("**Image APIs:**")
    for api, available in image_apis.items():
        status_class = "api-available" if available else "api-unavailable"
        status_text = "✅ Available" if available else "❌ Not configured"
        st.sidebar.markdown(
            f'<div class="api-status {status_class}">{api.title()}: {status_text}</div>',
            unsafe_allow_html=True
        )

def get_topic_suggestions():
    return [
        "Machine Learning Fundamentals",
        "Blockchain Technology",
        "Renewable Energy Sources",
        "Cybersecurity Best Practices",
        "Artificial Intelligence in Healthcare",
        "Digital Marketing Strategies",
        "Climate Change Solutions",
        "Data Science Applications",
        "Internet of Things (IoT)",
        "Quantum Computing Basics",
        "Remote Work Best Practices",
        "Sustainable Business Practices",
        "Mental Health Awareness",
        "Financial Planning and Investment",
        "Social Media Marketing",
        "The Future of Youth",
        "Deep Learning Applications",
        "Cloud Computing Trends",
        "Mobile App Development",
        "E-commerce Evolution"
    ]

def validate_api_setup(content_api, image_api):
    """Validate that selected APIs have proper configuration"""
    errors = []

    if content_api == 'gemini' and not os.getenv('GEMINI_API_KEY'):
        errors.append("Gemini API key not configured")

    if image_api == 'Pexels' and not os.getenv('PEXELS_API_KEY'):
        errors.append("Pexels API key not configured")
    elif image_api == 'Pixabay' and not os.getenv('PIXABAY_API_KEY'):
        errors.append("Pixabay API key not configured")

    return errors

def generate_presentation_with_progress(topic, num_slides, content_api, image_api,
                                      presentation_style, target_audience, include_images, detailed_content):
    """Generate the presentation with progress tracking"""
    
    # Create progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    try:
        # Initialize generator
        status_text.text("Initializing PPT Generator...")
        progress_bar.progress(10)
        
        generator = PPTGenerator()
        status_text.text("Generator initialized successfully!")
        progress_bar.progress(20)
        
        # Generate presentation
        status_text.text(f"Generating presentation on: {topic}")
        progress_bar.progress(30)
        
        # Create temporary file for the presentation
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pptx') as tmp_file:
            output_path = tmp_file.name
        
        # Generate the presentation
        output_file = generator.generate_presentation(
            topic=topic,
            num_slides=num_slides,
            output_path=output_path
        )
        
        progress_bar.progress(90)
        status_text.text("Presentation generated successfully!")
        progress_bar.progress(100)
        
        # Read the file for download
        with open(output_file, 'rb') as f:
            presentation_data = f.read()
        
        # Clean up temporary file
        os.unlink(output_file)
        
        return presentation_data, f"{topic.replace(' ', '_')}_presentation.pptx"
        
    except Exception as e:
        st.error(f"❌ Error generating presentation: {e}")
        return None, None

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🎨 AI PowerPoint Generator</h1>
        <p>Create professional presentations with AI-powered content and automatic image fallback</p>
    </div>
    """, unsafe_allow_html=True)

    # Check API availability
    content_apis, image_apis = check_api_availability()
    display_api_status(content_apis, image_apis)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("## 📝 Presentation Configuration")

        # Topic input
        topic_method = st.radio(
            "Choose how to enter your topic:",
            ["Select from suggestions", "Enter custom topic"],
            horizontal=True
        )

        if topic_method == "Select from suggestions":
            suggestions = get_topic_suggestions()
            selected_topic = st.selectbox("Choose a topic:", ["Select a topic..."] + suggestions)
            topic = "" if selected_topic == "Select a topic..." else selected_topic
        else:
            topic = st.text_area(
                "Enter your presentation topic:",
                placeholder="e.g., 'The Future of Artificial Intelligence in Education'",
                height=100
            )

        # Slide count
        num_slides = st.slider("Number of slides:", 3, 15, 8)

        # API selection
        col_api1, col_api2 = st.columns(2)
        with col_api1:
            available_content_apis = [api for api, available in content_apis.items() if available]
            if not available_content_apis:
                st.error("❌ No content generation APIs configured!")
                st.markdown("""
                <div class="warning-box">
                    <strong>Setup Required:</strong><br>
                    Please set your GEMINI_API_KEY in the .env file<br>
                    Get your API key from: <a href="https://makersuite.google.com/app/apikey" target="_blank">Google AI Studio</a>
                </div>
                """, unsafe_allow_html=True)
                st.stop()
            content_api = st.selectbox("Content Generation API:", available_content_apis)

        with col_api2:
            available_image_apis = [api for api, available in image_apis.items() if available]
            if not available_image_apis:
                st.warning("⚠️ No image APIs configured. Will use placeholder images.")
                image_api = "placeholder"
            else:
                image_api = st.selectbox("Image API:", available_image_apis)

        # Advanced options
        with st.expander("🔧 Advanced Options"):
            col_adv1, col_adv2 = st.columns(2)
            with col_adv1:
                presentation_style = st.selectbox("Presentation Style:", ["Professional", "Academic", "Creative", "Business"])
                target_audience = st.selectbox("Target Audience:", ["General", "Students", "Professionals", "Executives"])
            with col_adv2:
                include_images = st.checkbox("Include images in slides", value=True)
                detailed_content = st.checkbox("Generate detailed content", value=True)

        # Validate topic
        topic_valid = topic and topic.strip() and topic.strip() != "Select a topic..."

        if not topic_valid:
            st.warning("⚠️ Please enter or select a valid topic before generating.")

        # Generate button
        generate_button = st.button(
            "🚀 Generate Presentation",
            type="primary",
            disabled=not topic_valid,
            use_container_width=True
        )

        # Handle generation
        if generate_button and topic_valid:
            api_errors = validate_api_setup(content_api, image_api)
            if api_errors:
                for error in api_errors:
                    st.error(f"❌ {error}")
                st.info("💡 Please configure your API keys in the .env file and restart.")
            else:
                topic_cleaned = topic.strip()
                if len(topic_cleaned) < 5:
                    st.error("❌ Topic too short.")
                elif len(topic_cleaned) > 200:
                    st.error("❌ Topic too long.")
                else:
                    # Generate presentation
                    presentation_data, filename = generate_presentation_with_progress(
                        topic_cleaned, num_slides, content_api, image_api,
                        presentation_style, target_audience, include_images, detailed_content
                    )
                    
                    if presentation_data and filename:
                        # Display success message
                        st.markdown("""
                        <div class="success-box">
                            <strong>✅ Presentation Generated Successfully!</strong><br>
                            Your AI-powered presentation is ready for download.
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Download button
                        st.download_button(
                            label="📥 Download Presentation",
                            data=presentation_data,
                            file_name=filename,
                            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                            use_container_width=True
                        )
                        
                        # Add to recent generations
                        if 'recent_presentations' not in st.session_state:
                            st.session_state.recent_presentations = []
                        
                        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                        st.session_state.recent_presentations.append({
                            'topic': topic_cleaned,
                            'timestamp': timestamp,
                            'filename': filename
                        })

    with col2:
        st.markdown("## ℹ️ Features")
        for feature in [
            "🤖 AI-powered content generation",
            "🖼️ Automatic image fallback (Pixabay → Pexels → Placeholder)",
            "📊 Professional slide layouts",
            "⚡ Fast generation (2-5 minutes)",
            "📱 Responsive design templates",
            "🎨 Multiple presentation styles",
            "📐 Fixed text alignment issues",
            "🔄 Robust error handling"
        ]:
            st.markdown(f'<div class="feature-box">{feature}</div>', unsafe_allow_html=True)
        
        # Show fallback strategy
        if image_apis['pixabay'] or image_apis['pexels']:
            st.markdown("## 🔄 Image Strategy")
            st.markdown("""
            <div class="feature-box">
                <strong>Automatic Fallback:</strong><br>
                1️⃣ Pixabay (Primary)<br>
                2️⃣ Pexels (Fallback)<br>
                3️⃣ Placeholder (Final)
            </div>
            """, unsafe_allow_html=True)

def display_sidebar_info():
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📋 Recent Generations")
    if 'recent_presentations' not in st.session_state:
        st.session_state.recent_presentations = []
    
    if st.session_state.recent_presentations:
        for p in st.session_state.recent_presentations[-5:]:
            st.sidebar.text(f"• {p['topic'][:30]}...")
            st.sidebar.text(f"  {p['timestamp']}")
    else:
        st.sidebar.text("No recent presentations")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🛠️ Quick Actions")
    
    if st.sidebar.button("🧪 Test Image APIs"):
        st.sidebar.info("Run: python quick_test.py")
    
    if st.sidebar.button("🔧 Setup Guide"):
        st.sidebar.info("Run: python setup.py")

if __name__ == "__main__":
    main()
    display_sidebar_info()
