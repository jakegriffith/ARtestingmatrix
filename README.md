# 🟩 Matrix AR - Code Rain Experience

A web-based augmented reality experience that displays Matrix-style green code rain floating in 3D space when pointing your phone's camera at a Hiro marker. Built with AR.js and A-Frame.

![Matrix AR Demo](https://img.shields.io/badge/AR-Matrix%20Code%20Rain-00ff00?style=for-the-badge)
![Platform](https://img.shields.io/badge/platform-mobile%20web-blue?style=for-the-badge)
![License](https://img.shields.io/badge/license-free%20to%20use-green?style=for-the-badge)

## ✨ Features

- 🎯 **Marker-based AR** using Hiro pattern (no app installation required)
- 💚 **Bright green Matrix code** (#00ff00) streaming in 3D
- ⚡ **Dynamic animations** - characters change randomly
- 👁️ **Glitch effects** - corrupted text appears and disappears
- 📱 **Mobile-first** - works directly in phone browsers
- 🌊 **Multiple streams** floating at different positions and depths
- 🔮 **3D space** - code surrounds the marker in all directions

## 🚀 Quick Start (GitHub Pages - RECOMMENDED)

This is the **easiest and most reliable method** for testing on your phone:

1. **Fork or create a new repository** on GitHub
2. **Upload `matrix-ar.html`** to your repository
3. **Enable GitHub Pages:**
   - Go to Settings → Pages
   - Source: Deploy from branch
   - Branch: main (or master)
   - Click Save
4. **Access your site:**
   - GitHub will provide a URL like: `https://yourusername.github.io/reponame/matrix-ar.html`
5. **Open on your phone** and allow camera access
6. **Point at Hiro marker** (see below for marker)

### ✅ Why GitHub Pages?
- ✓ Completely **FREE** (no costs)
- ✓ **HTTPS by default** (required for camera)
- ✓ **No server setup** needed
- ✓ Works from **anywhere** (not just local network)
- ✓ Easy to share with others

## 🎯 Getting the Hiro Marker

You need a Hiro marker for the AR to work. Here's how to get one:

### Option 1: Download and Print
Download the marker from:
```
https://raw.githubusercontent.com/AR-js-org/AR.js/master/data/images/hiro.png
```

Or search Google for "AR.js Hiro marker" and use any result.

### Option 2: Display on Screen
- Open the marker image on your computer/tablet
- Point your phone camera at the screen
- Works just as well as printed!

### What does it look like?
The Hiro marker is a thick black square border with a distinctive pattern inside (looks like nested squares).

## 🖥️ Local Testing Options

### Method 1: Python Server (Simple)

```bash
# Start the server
python3 serve.py

# The server will display URLs for access
# Open on your phone: http://YOUR-IP:8000/matrix-ar.html
```

⚠️ **Note:** May not work on all browsers due to HTTPS requirement for camera access.

### Method 2: Using ngrok (Most Reliable for Local)

```bash
# Terminal 1: Start Python server
python3 serve.py

# Terminal 2: Start ngrok
ngrok http 8000

# Use the HTTPS URL that ngrok provides
# Example: https://abc123.ngrok.io/matrix-ar.html
```

Install ngrok:
```bash
# macOS
brew install ngrok

# Or download from
https://ngrok.com/download
```

## 📱 How to Use

1. **Open the URL** on your phone's browser (Chrome/Safari recommended)
2. **Allow camera access** when prompted
3. **Point camera at Hiro marker**
4. **Watch reality leak digital code!** 🟩⚡

### 💡 Tips for Best Results

- 📸 **Good lighting** - Ensure the marker is well-lit
- 📐 **Flat surface** - Keep marker on flat surface or display
- 📏 **Distance** - Hold phone 20-40cm from marker
- 🎯 **Steady hand** - Keep phone relatively steady
- 🔄 **Angle** - Try to keep marker face-on to camera
- 🖼️ **Size** - Marker should take up good portion of view

## 🎨 Customization

### Change Colors
Find and replace `color="#00ff00"` in `matrix-ar.html` with any hex color:
- Red Matrix: `color="#ff0000"`
- Blue Matrix: `color="#00ffff"`
- Purple Matrix: `color="#ff00ff"`

### Add More Streams
Copy any `<a-text>` block and change:
- `id="stream9"` (unique ID)
- `position="x y z"` (new 3D position)
- `rotation="x y z"` (angle in space)

### Adjust Animation Speed
In the JavaScript, modify the `animateStream()` calls:
```javascript
animateStream('stream1', 100, matrixChars, 8);  // faster (100ms)
animateStream('stream2', 300, matrixChars, 6);  // slower (300ms)
```

### More Glitch Characters
Edit the `glitchChars` variable:
```javascript
const glitchChars = '█▓▒░▄▀■□▪▫¶§†‡∆∇∞≈≠±×÷√∑∫☠️⚠️🔥';
```

## 🛠️ Technical Details

- **AR.js 3.4.5** - Marker-based AR tracking
- **A-Frame 1.4.2** - WebXR framework
- **Hiro Marker** - Default AR.js test pattern
- **Pure HTML/JS** - No build process required
- **Mobile-first** - Optimized for phone cameras

## 🐛 Troubleshooting

### Camera Won't Work
- **Problem:** Browser blocks camera access
- **Solution:** Use HTTPS (GitHub Pages or ngrok)

### Marker Not Detected
- **Check lighting** - Need good illumination
- **Check marker quality** - Print clearly or use high-res screen
- **Check distance** - Try moving closer/farther
- **Check angle** - Keep marker face-on

### Code Not Appearing
- **Open browser console** (for debugging)
- **Check marker detection** - Console logs when marker found
- **Try refreshing** the page
- **Ensure good lighting**

### Performance Issues
- **Close other apps** on phone
- **Use recent phone** (2019+ recommended)
- **Try Chrome** instead of Safari (or vice versa)

## 📂 Project Structure

```
matrix-ar/
├── matrix-ar.html    # Main AR experience (self-contained)
├── serve.py          # Local Python server
└── README.md         # This file
```

## 🎮 How It Works

1. **AR.js** detects the Hiro marker pattern in camera feed
2. **A-Frame** creates 3D scene anchored to marker
3. **JavaScript** animates text entities with:
   - Random character generation
   - Opacity flickering (glitch effect)
   - Position floating (3D movement)
   - Timed updates for "code rain" effect

## 🌟 What Makes This Cool

- **No app required** - runs in any mobile browser
- **Instant loading** - single HTML file
- **Reality augmentation** - code appears in real space
- **3D positioning** - streams float around marker
- **Dynamic effects** - always changing, never static
- **Cyberpunk aesthetic** - bright green on black

## 📝 License

Free to use, modify, and share. No attribution required.

## 🤝 Contributing

Feel free to:
- Add more effects
- Improve animations
- Create new marker patterns
- Share your modifications

## 💚 Made with Matrix Love

*"What is real? How do you define 'real'?"*

---

**Need help?** Check the troubleshooting section or open an issue.

**Want to share your creation?** Tag it with #MatrixAR
