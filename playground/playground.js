function runCode() {
    const htmlContent = htmlEditor.getValue();
    const cssContent = cssEditor.getValue();
    const jsContent = jsEditor.getValue();

    const combinedContent = `
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Code Output</title>
            <style>
                ${cssContent}
            </style>
        </head>
        <body>
            ${htmlContent}
            <script>
                try {
                    ${jsContent}
                } catch (error) {
                    console.error("JavaScript Error:", error.message);
                    document.body.innerHTML += '<div style="color: red; background: rgba(255,0,0,0.1); padding: 10px; margin-top: 10px; border-left: 4px solid red; font-family: monospace;">Error: ' + error.message + '</div>';
                }
            </script>
        </body>
        </html>
    `;

    // Write to the iframe
    const iframe = document.getElementById('output');
    const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
    iframeDoc.open();
    iframeDoc.write(combinedContent);
    iframeDoc.close();

    htmlEditor.refresh();
    cssEditor.refresh();
    jsEditor.refresh();
}

const htmlEditor = CodeMirror.fromTextArea(document.getElementById('html-code'), {
    mode: 'xml',
    theme: 'monokai',
    lineNumbers: true,
    autoCloseTags: true,
    autoCloseBrackets: true,
    matchBrackets: true,
    indentUnit: 4,
    tabSize: 4,
    lineWrapping: true,
    extraKeys: {
        "Ctrl-C": function(cm) {
            const selectedText = cm.getSelection();
            if (selectedText) {
                navigator.clipboard.writeText(selectedText);
            } else {
                navigator.clipboard.writeText(cm.getValue());
            }
        },
        "Ctrl-V": function(cm) {
            navigator.clipboard.readText().then(text => {
                const currentContent = cm.getValue();
                const cursor = cm.getCursor();
                const newContent = currentContent.slice(0, cm.indexFromPos(cursor)) + text + currentContent.slice(cm.indexFromPos(cursor));
                cm.setValue(newContent);
                cm.setCursor(cursor);
            });
        }
    }
});

const cssEditor = CodeMirror.fromTextArea(document.getElementById('css-code'), {
    mode: 'css',
    theme: 'monokai',
    lineNumbers: true,
    autoCloseBrackets: true,
    matchBrackets: true,
    indentUnit: 4,
    tabSize: 4,
    lineWrapping: true,
    extraKeys: {
        "Ctrl-C": function(cm) {
            const selectedText = cm.getSelection();
            if (selectedText) {
                navigator.clipboard.writeText(selectedText);
            } else {
                navigator.clipboard.writeText(cm.getValue());
            }
        },
        "Ctrl-V": function(cm) {
            navigator.clipboard.readText().then(text => {
                const currentContent = cm.getValue();
                const cursor = cm.getCursor();
                const newContent = currentContent.slice(0, cm.indexFromPos(cursor)) + text + currentContent.slice(cm.indexFromPos(cursor));
                cm.setValue(newContent);
                cm.setCursor(cursor);
            });
        }
    }
});

const jsEditor = CodeMirror.fromTextArea(document.getElementById('js-code'), {
    mode: 'javascript',
    theme: 'monokai',
    lineNumbers: true,
    autoCloseBrackets: true,
    matchBrackets: true,
    indentUnit: 4,
    tabSize: 4,
    lineWrapping: true,
    extraKeys: {
        "Ctrl-C": function(cm) {
            const selectedText = cm.getSelection();
            if (selectedText) {
                navigator.clipboard.writeText(selectedText);
            } else {
                navigator.clipboard.writeText(cm.getValue());
            }
        },
        "Ctrl-V": function(cm) {
            navigator.clipboard.readText().then(text => {
                const currentContent = cm.getValue();
                const cursor = cm.getCursor();
                const newContent = currentContent.slice(0, cm.indexFromPos(cursor)) + text + currentContent.slice(cm.indexFromPos(cursor));
                cm.setValue(newContent);
                cm.setCursor(cursor);
            });
        }
    }
});

// Set default content
const defaultHtml = `<div class="container">
    <h1>Welcome to the Code Playground</h1>
    <p>Start coding in the editors above!</p>
</div>`;

const defaultCss = `@import url('https://fonts.googleapis.com/css2?family=Bree+Serif&family=Caveat:wght@400;700&family=Lobster&family=Monoton&family=Open+Sans:ital,wght@0,400;0,700;1,400;1,700&family=Playfair+Display+SC:ital,wght@0,400;0,700;1,700&family=Playfair+Display:ital,wght@0,400;0,700;1,700&family=Roboto:ital,wght@0,400;0,700;1,400;1,700&family=Source+Sans+Pro:ital,wght@0,400;0,700;1,700&family=Work+Sans:ital,wght@0,400;0,700;1,700&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    min-height: 100vh;
    font-family: 'Roboto', sans-serif;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
}

.container {
    width: 100%;
    max-width: 1200px;
    padding: 2rem;
    background: rgba(255, 255, 255, 0.9);
    border-radius: 15px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(10px);
    text-align: center;
}

h1 {
    color: #333;
    margin-bottom: 1rem;
}

p {
    color: #666;
}`;

const defaultJs = `// Add your JavaScript code here
document.addEventListener('DOMContentLoaded', function() {
    console.log('Ready to code!');
});`;

// Set default content
htmlEditor.setValue(defaultHtml);
cssEditor.setValue(defaultCss);
jsEditor.setValue(defaultJs);

// Function to reset editor content
function resetEditor(editor, defaultContent) {
    editor.setValue(defaultContent);
    editor.refresh();
}

// Add reset buttons to panel headers
const htmlHeader = document.querySelector('[data-editor="html"]').parentElement;
const cssHeader = document.querySelector('[data-editor="css"]').parentElement;
const jsHeader = document.querySelector('[data-editor="js"]').parentElement;

// Create and add reset buttons
[htmlHeader, cssHeader, jsHeader].forEach((header, index) => {
    const resetButton = document.createElement('button');
    resetButton.className = 'reset-button';
    resetButton.innerHTML = '<ion-icon name="refresh"></ion-icon>';
    resetButton.title = 'Reset to default';
    resetButton.onclick = () => {
        switch(index) {
            case 0:
                resetEditor(htmlEditor, defaultHtml);
                break;
            case 1:
                resetEditor(cssEditor, defaultCss);
                break;
            case 2:
                resetEditor(jsEditor, defaultJs);
                break;
        }
    };
    header.appendChild(resetButton);
});

// Tab switching functionality
const tabButtons = document.querySelectorAll('.tab-button');
const editorWrappers = document.querySelectorAll('.editor-wrapper');

tabButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Remove active class from all buttons and editors
        tabButtons.forEach(btn => btn.classList.remove('active'));
        editorWrappers.forEach(editor => editor.classList.remove('active'));

        // Add active class to clicked button and corresponding editor
        button.classList.add('active');
        const editorType = button.dataset.editor;
        document.getElementById(`${editorType}-editor`).classList.add('active');

        // Refresh the active editor
        switch(editorType) {
            case 'html':
                htmlEditor.refresh();
                break;
            case 'css':
                cssEditor.refresh();
                break;
            case 'js':
                jsEditor.refresh();
                break;
        }
    });
});

// Resizer functionality
const resizer = document.querySelector('.resizer');
const leftPanel = document.querySelector('.code-panel');
const rightPanel = document.querySelector('.output-panel');
const editorContainer = document.querySelector('.editor-container');

let isResizing = false;
let startX;
let startLeftWidth;

// Add visual feedback when hovering over the resizer
resizer.addEventListener('mouseover', () => {
    resizer.classList.add('hovered');
});

resizer.addEventListener('mouseout', () => {
    if (!isResizing) {
        resizer.classList.remove('hovered');
    }
});

resizer.addEventListener('mousedown', (e) => {
    isResizing = true;
    startX = e.pageX;
    startLeftWidth = leftPanel.offsetWidth;
    
    // Add active class for styling
    resizer.classList.add('active');
    editorContainer.classList.add('resizing');
    
    // Change cursor for the entire document while resizing
    document.body.style.cursor = 'col-resize';
    
    // Prevent text selection during resize
    document.body.style.userSelect = 'none';
    document.body.style.pointerEvents = 'none';
});

document.addEventListener('mousemove', (e) => {
    if (!isResizing) return;

    const diffX = e.pageX - startX;
    const containerWidth = resizer.parentNode.offsetWidth;
    const newLeftWidth = ((startLeftWidth + diffX) * 100) / containerWidth;

    // Add smooth transition during resize
    leftPanel.style.transition = 'none';
    rightPanel.style.transition = 'none';

    // Set minimum and maximum widths for panels
    if (newLeftWidth > 20 && newLeftWidth < 80) {
        leftPanel.style.width = `${newLeftWidth}%`;
        rightPanel.style.width = `${100 - newLeftWidth}%`;
        
        // Refresh editors to prevent rendering issues
        if (diffX % 10 === 0) {
            htmlEditor.refresh();
            cssEditor.refresh();
            jsEditor.refresh();
        }
    }
});

document.addEventListener('mouseup', () => {
    if (!isResizing) return;
    
    isResizing = false;
    
    // Remove active classes
    resizer.classList.remove('active');
    editorContainer.classList.remove('resizing');
    
    // Reset cursor and text selection
    document.body.style.cursor = 'default';
    document.body.style.userSelect = '';
    document.body.style.pointerEvents = '';
    
    // Re-enable smooth transitions
    leftPanel.style.transition = 'width 0.2s ease';
    rightPanel.style.transition = 'width 0.2s ease';
    
    // Add small delay before refreshing editors
    setTimeout(() => {
        htmlEditor.refresh();
        cssEditor.refresh();
        jsEditor.refresh();
    }, 200);
});

// Double-click to reset to 50/50 split
resizer.addEventListener('dblclick', () => {
    leftPanel.style.transition = 'width 0.3s ease';
    rightPanel.style.transition = 'width 0.3s ease';
    
    leftPanel.style.width = '50%';
    rightPanel.style.width = '50%';
    
    setTimeout(() => {
        htmlEditor.refresh();
        cssEditor.refresh();
        jsEditor.refresh();
    }, 300);
});

// Run code functionality
const runButton = document.getElementById('run-btn');
const output = document.getElementById('output');

runButton.addEventListener('click', runCode);

// Run code on startup
runCode();

// Navbar functionality
const hamburger = document.querySelector('.hamburger');
const navbar = document.querySelector('.left-navbar');
    
hamburger.addEventListener('click', function() {
    navbar.classList.toggle('expanded');
});

// Autorun functionality
const autorunCheckbox = document.getElementById('autorun');
let autorunEnabled = false;
let typingTimer;
const doneTypingInterval = 1000; // Time in ms (1 second)

// Set up autorun functionality
autorunCheckbox.addEventListener('change', function() {
    autorunEnabled = this.checked;
    if (autorunEnabled) {
        // Run immediately when autorun is enabled
        runCode();
    }
});

// Function to handle code changes with debounce
function codeChanged() {
    if (autorunEnabled) {
        clearTimeout(typingTimer);
        typingTimer = setTimeout(runCode, doneTypingInterval);
    }
}

// Add input event listeners to all code editors
htmlEditor.on('change', codeChanged);
cssEditor.on('change', codeChanged);
jsEditor.on('change', codeChanged);

// Add keyboard shortcut for running code (Ctrl+Enter)
document.addEventListener('keydown', function(e) {
    if (e.ctrlKey && e.key === 'Enter') {
        e.preventDefault();
        runCode();
    }
});