
// DOM Elements
const chatMessages = document.getElementById('chatMessages');
const userInput = document.getElementById('userInput');
const sendButton = document.getElementById('sendButton');
const micButton = document.getElementById('micButton');
const waveBars = document.querySelectorAll('.wave span');

// Voice Recognition Setup
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.continuous = false;
recognition.interimResults = false;
recognition.lang = 'en-US';

let isListening = false;

// Toggle wave animation
function toggleWaveAnimation(isActive) {
    waveBars.forEach(span => {
        span.style.animationPlayState = isActive ? 'running' : 'paused';
    });
}


// Add message to chat
function addMessage(message, isUser = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isUser ? 'user_message' : 'ai_message'}`;
    messageDiv.textContent = message;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Handle text input
function handleTextInput() {
    const message = userInput.value.trim();
    if (message) {
        addMessage(message, true);
        userInput.value = '';
        // Simulate AI response (you can replace this with actual AI integration)
        setTimeout(() => {
            addMessage("I'm processing your message...");
        }, 500);
    }
}

// Handle voice input
function toggleVoiceInput() {
    if (!isListening) {
        recognition.start();
        isListening = true;
        micButton.style.background = '#dc3545';
        toggleWaveAnimation(true);
    } else {
        recognition.stop();
        isListening = false;
        micButton.style.background = '#28a745';
        toggleWaveAnimation(false);
    }
}

// Event Listeners
sendButton.addEventListener('click', handleTextInput);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        handleTextInput();
    }
});
micButton.addEventListener('click', toggleVoiceInput);

// Voice Recognition Events
recognition.onresult = (event) => {
    const message = event.results[0][0].transcript;
    addMessage(message, true);
    // Simulate AI response (you can replace this with actual AI integration)
    setTimeout(() => {
        addMessage("I heard you say: " + message);
    }, 500);
};

// Speak message using SpeechSynthesis
function speakMessage(message) {
    const utterance = new SpeechSynthesisUtterance(message);
    utterance.lang = 'en-US';
    utterance.rate = 3; // Increase speaking speed (1 is normal, 2 is double speed)
    window.speechSynthesis.speak(utterance);
}
// Add message to chat
function addMessage(message, isUser = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isUser ? 'user_message' : 'ai_message'}`;
    messageDiv.textContent = message;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    // Speak only AI messages
    if (!isUser) {
        speakMessage(message);
    }
}

recognition.onend = () => {
    isListening = false;
    micButton.style.background = '#28a745';
    toggleWaveAnimation(false);
};

recognition.onerror = (event) => {
    console.error('Speech recognition error:', event.error);
    isListening = false;
    micButton.style.background = '#28a745';
    toggleWaveAnimation(false);
};


// ...existing code...

function handleTextInput() {
    const message = userInput.value.trim();
    if (message) {
        addMessage(message, true);
        userInput.value = '';
        // Check for "open youtube" command
        if (message.toLowerCase().includes('youtube')){
            window.open('https://www.youtube.com', '_blank');
            setTimeout(() => {
                addMessage("Opening YouTube...");
            }, 500);
            return;
        }
        else if (message.toLowerCase().includes('github')){
            window.open('https://www.github.com', '_blank');
            setTimeout(() => {
                addMessage("opening github...");

            }, 500);
            return;
        }
        else if (message.toLowerCase().includes('google')){
            window.open('https://www.google.com', '_blank');
            setTimeout(() => {
                addMessage("opening google...");

            }, 500);
            return;
        }
        else if (message.toLowerCase().includes('instagram')){
            window.open('https://www.instagram.com', '_blank');
            setTimeout(() => {
                addMessage("opening instagram...");

            }, 500);
            return;
        }
        else if (message.toLowerCase().includes('whatsapp')){
            window.open('https://www.whatsapp.com', '_blank');
            setTimeout(() => {
                addMessage("opening github...");

            }, 500);
            return;
        }
        else if (message.toLowerCase().includes('time')){
            const now = new Date();
            const timeString = now.toLocaleDateString();
            setTimeout(() => {
                addMessage("the current time is : " + timeString);

            } , 500);vfv
            return;
        }    
        // Simulate AI response (you can replace this with actual AI integration)
        setTimeout(() => {
            addMessage("I'm processing your message...");
        }, 500);
    }
}

// ...existing code...

