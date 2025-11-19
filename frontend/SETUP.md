# Frontend Setup Guide

## Installation

First, install the required dependencies:

```bash
cd frontend
npm install axios uuid
```

## Development

1. Make sure your backend is running on `http://127.0.0.1:8000`
2. Start the frontend development server:

```bash
npm run dev
```

3. Open your browser to `http://localhost:5173`

## Features

### Chat Interface

- Send messages to the ZUS Coffee AI Agent
- Receive responses with product info, outlet locations, and calculations
- Conversation history is automatically saved to localStorage

### Quick Actions

- **Calculate**: Click to perform math calculations (e.g., `/calc 200 * 0.8`)
- **Products**: Search for drinkware products
- **Outlets**: Find ZUS Coffee outlet locations
- **Help**: Get information about available commands

### Keyboard Shortcuts

- **Enter**: Send message
- **Shift+Enter**: New line in message

### Clear History

- Click the "🗑️ Clear" button in the header to reset the conversation

## API Configuration

The frontend connects to the backend via environment variables:

- **Development**: `.env` (uses `http://127.0.0.1:8000`)
- **Production**: `.env.production` (update with your Render URL)

## File Structure

```
frontend/src/
├── components/
│   ├── AgentMessage.vue       # Agent response bubble
│   ├── ChatWindow.vue         # Main chat display area
│   ├── Composer.vue           # Message input field
│   ├── QuickActions.vue       # Quick action buttons
│   └── UserMessage.vue        # User message bubble
├── composables/
│   └── useChat.ts             # Chat state management & localStorage
├── services/
│   └── api.ts                 # Backend API calls
├── types/
│   └── chat.ts                # TypeScript interfaces
├── App.vue                    # Main application component
└── style.css                  # Global styles
```

## Testing

Test the following scenarios:

1. **Basic Chat**: Send "Hello" and get a response
2. **Calculator**: Send `/calc 150 * 0.9`
3. **Products**: Send "Show me tumblers under $30"
4. **Outlets**: Send "Find outlets in Petaling Jaya"
5. **Persistence**: Refresh the page and verify history is restored

## Building for Production

```bash
npm run build
```

The build output will be in the `dist/` folder, ready for deployment to Vercel.

## Deployment Notes

Before deploying to Vercel:

1. Update `.env.production` with your Render backend URL
2. Add your Vercel domain to the CORS configuration in `backend/app/main.py`
3. Ensure environment variables are set in Vercel dashboard
