{
    "name": "CSS Selectors & Specificity",
    "description": "Learn about different CSS selectors and how specificity affects styles.",
    "puzzles": [
        {
            "question": "Select all paragraphs inside a div.",
            "solution": "div p { color: blue; }",
            "hint": "Use descendant selector.",
            "test": "div p" in code
        },
        {
            "question": "Select an element with the ID 'header'.",
            "solution": "#header { font-size: 20px; }",
            "hint": "Use # for ID selectors.",
            "test": "#header" in code
        },
        {
            "question": "Select all elements with class 'btn'.",
            "solution": ".btn { background-color: red; }",
            "hint": "Use . for class selectors.",
            "test": ".btn" in code
        },
        {
            "question": "Select only direct children paragraphs inside a div.",
            "solution": "div > p { color: green; }",
            "hint": "Use the child combinator (>).
            "test": "div > p" in code
        },
        {
            "question": "Select all links that are hovered over.",
            "solution": "a:hover { text-decoration: underline; }",
            "hint": "Use the :hover pseudo-class.",
            "test": "a:hover" in code
        },
        {
            "question": "Select all checked checkboxes.",
            "solution": "input[type='checkbox']:checked { border: 2px solid green; }",
            "hint": "Use :checked pseudo-class.",
            "test": "input[type='checkbox']:checked" in code
        },
        {
            "question": "Select the first child of every div.",
            "solution": "div:first-child { font-weight: bold; }",
            "hint": "Use :first-child pseudo-class.",
            "test": "div:first-child" in code
        },
        {
            "question": "Select every odd numbered row in a table.",
            "solution": "tr:nth-child(odd) { background-color: gray; }",
            "hint": "Use :nth-child() pseudo-class.",
            "test": "tr:nth-child(odd)" in code
        },
        {
            "question": "Select input fields that are required.",
            "solution": "input:required { border: 1px solid red; }",
            "hint": "Use :required pseudo-class.",
            "test": "input:required" in code
        },
        {
            "question": "Select elements with a specific attribute.",
            "solution": "[data-info] { color: orange; }",
            "hint": "Use attribute selectors.",
            "test": "[data-info]" in code
        },
        {
            "question": "Select only the first letter of each paragraph.",
            "solution": "p::first-letter { font-size: 24px; }",
            "hint": "Use ::first-letter pseudo-element.",
            "test": "p::first-letter" in code
        },
        {
            "question": "Select all list items that are the last child in their parent.",
            "solution": "li:last-child { font-style: italic; }",
            "hint": "Use :last-child pseudo-class.",
            "test": "li:last-child" in code
        },
        {
            "question": "Select all buttons that are disabled.",
            "solution": "button:disabled { background-color: gray; }",
            "hint": "Use :disabled pseudo-class.",
            "test": "button:disabled" in code
        },
        {
            "question": "Select elements that have a title attribute.",
            "solution": "[title] { text-decoration: underline; }",
            "hint": "Use attribute selectors.",
            "test": "[title]" in code
        },
        {
            "question": "Select the last paragraph inside a div.",
            "solution": "div p:last-of-type { font-weight: bold; }",
            "hint": "Use :last-of-type pseudo-class.",
            "test": "div p:last-of-type" in code
        }
    ]
}
{
    "name": "Colors & Backgrounds",
    "description": "Learn about applying colors and backgrounds in CSS.",
    "puzzles": [
        {
            "question": "Set the text color of all paragraphs to blue.",
            "solution": "p { color: blue; }",
            "hint": "Use the color property.",
            "test": "p { color:" in code
        },
        {
            "question": "Set the background color of the body to light gray.",
            "solution": "body { background-color: lightgray; }",
            "hint": "Use background-color property.",
            "test": "body { background-color:" in code
        },
        {
            "question": "Apply a linear gradient from red to yellow as a background to a div.",
            "solution": "div { background: linear-gradient(red, yellow); }",
            "hint": "Use linear-gradient function.",
            "test": "linear-gradient" in code
        },
        {
            "question": "Set the background image of a div using 'background-image'.",
            "solution": "div { background-image: url('image.jpg'); }",
            "hint": "Use background-image property.",
            "test": "background-image" in code
        },
        {
            "question": "Make the text color of all h1 elements red.",
            "solution": "h1 { color: red; }",
            "hint": "Use color property.",
            "test": "h1 { color:" in code
        },
        {
            "question": "Set the background color of even table rows to light blue.",
            "solution": "tr:nth-child(even) { background-color: lightblue; }",
            "hint": "Use nth-child selector.",
            "test": "tr:nth-child(even)" in code
        },
        {
            "question": "Set the text color of a button to white and background to black.",
            "solution": "button { color: white; background-color: black; }",
            "hint": "Use color and background-color together.",
            "test": "button { color:" in code
        },
        {
            "question": "Make the background image cover the entire div.",
            "solution": "div { background-size: cover; }",
            "hint": "Use background-size property.",
            "test": "background-size: cover" in code
        },
        {
            "question": "Apply a semi-transparent black background to a div.",
            "solution": "div { background-color: rgba(0, 0, 0, 0.5); }",
            "hint": "Use rgba function.",
            "test": "rgba(" in code
        },
        {
            "question": "Apply a radial gradient from blue to white as a background.",
            "solution": "div { background: radial-gradient(blue, white); }",
            "hint": "Use radial-gradient function.",
            "test": "radial-gradient" in code
        },
        {
            "question": "Make the background image fixed when scrolling.",
            "solution": "div { background-attachment: fixed; }",
            "hint": "Use background-attachment property.",
            "test": "background-attachment: fixed" in code
        },
        {
            "question": "Set a background image that does not repeat.",
            "solution": "div { background-repeat: no-repeat; }",
            "hint": "Use background-repeat property.",
            "test": "background-repeat: no-repeat" in code
        },
        {
            "question": "Change the text color of a link when hovered to green.",
            "solution": "a:hover { color: green; }",
            "hint": "Use :hover pseudo-class.",
            "test": "a:hover" in code
        },
        {
            "question": "Make the background color of a button change when hovered.",
            "solution": "button:hover { background-color: orange; }",
            "hint": "Use :hover pseudo-class.",
            "test": "button:hover" in code
        },
        {
            "question": "Set the text color of the first letter of a paragraph to red.",
            "solution": "p::first-letter { color: red; }",
            "hint": "Use ::first-letter pseudo-element.",
            "test": "p::first-letter" in code
        }
    ]
}{
    "name": "Box Model",
    "description": "Learn about the CSS Box Model, including margins, padding, borders, and width/height.",
    "puzzles": [
        {
            "question": "Set the width of a div to 200px.",
            "solution": "div { width: 200px; }",
            "hint": "Use the width property.",
            "test": "div { width:" in code
        },
        {
            "question": "Set the height of a div to 150px.",
            "solution": "div { height: 150px; }",
            "hint": "Use the height property.",
            "test": "div { height:" in code
        },
        {
            "question": "Apply a margin of 20px to all sides of a div.",
            "solution": "div { margin: 20px; }",
            "hint": "Use the margin property.",
            "test": "div { margin:" in code
        },
        {
            "question": "Add 10px of padding to all sides of a div.",
            "solution": "div { padding: 10px; }",
            "hint": "Use the padding property.",
            "test": "div { padding:" in code
        },
        {
            "question": "Set a solid black border of 2px around a div.",
            "solution": "div { border: 2px solid black; }",
            "hint": "Use the border property.",
            "test": "div { border:" in code
        },
        {
            "question": "Set different margins: 10px top, 15px right, 20px bottom, and 25px left.",
            "solution": "div { margin: 10px 15px 20px 25px; }",
            "hint": "Use the margin shorthand.",
            "test": "margin:" in code
        },
        {
            "question": "Add a border-radius of 10px to a div.",
            "solution": "div { border-radius: 10px; }",
            "hint": "Use border-radius property.",
            "test": "border-radius" in code
        },
        {
            "question": "Set the box-sizing of a div to border-box.",
            "solution": "div { box-sizing: border-box; }",
            "hint": "Use box-sizing property.",
            "test": "box-sizing: border-box" in code
        },
        {
            "question": "Apply a box-shadow to a div with 5px horizontal, 5px vertical, 10px blur, and gray color.",
            "solution": "div { box-shadow: 5px 5px 10px gray; }",
            "hint": "Use box-shadow property.",
            "test": "box-shadow" in code
        },
        {
            "question": "Add an outline of 3px dashed red around a div.",
            "solution": "div { outline: 3px dashed red; }",
            "hint": "Use the outline property.",
            "test": "outline:" in code
        },
        {
            "question": "Make the padding of a div only apply to the left side (30px).",
            "solution": "div { padding-left: 30px; }",
            "hint": "Use padding-left property.",
            "test": "padding-left" in code
        },
        {
            "question": "Apply a double blue border of 4px around a div.",
            "solution": "div { border: 4px double blue; }",
            "hint": "Use border style with double.",
            "test": "border: 4px double" in code
        },
        {
            "question": "Set the max-width of a div to 400px.",
            "solution": "div { max-width: 400px; }",
            "hint": "Use max-width property.",
            "test": "max-width" in code
        },
        {
            "question": "Apply a min-height of 100px to a div.",
            "solution": "div { min-height: 100px; }",
            "hint": "Use min-height property.",
            "test": "min-height" in code
        },
        {
            "question": "Add a dotted green border on the right side of a div.",
            "solution": "div { border-right: 2px dotted green; }",
            "hint": "Use border-right property.",
            "test": "border-right" in code
        }
    ]
}
{
    "name": "Flexbox",
    "description": "Learn about CSS Flexbox, a layout model that allows elements to align and distribute space within a container.",
    "puzzles": [
        {
            "question": "Make a container a flex container.",
            "solution": "div { display: flex; }",
            "hint": "Use display property with flex.",
            "test": "display: flex" in code
        },
        {
            "question": "Align items in the center along the main axis.",
            "solution": "div { justify-content: center; }",
            "hint": "Use justify-content property.",
            "test": "justify-content: center" in code
        },
        {
            "question": "Align items to the start along the cross axis.",
            "solution": "div { align-items: flex-start; }",
            "hint": "Use align-items property.",
            "test": "align-items: flex-start" in code
        },
        {
            "question": "Make flex items wrap to the next row if necessary.",
            "solution": "div { flex-wrap: wrap; }",
            "hint": "Use flex-wrap property.",
            "test": "flex-wrap: wrap" in code
        },
        {
            "question": "Set the direction of flex items to column.",
            "solution": "div { flex-direction: column; }",
            "hint": "Use flex-direction property.",
            "test": "flex-direction: column" in code
        },
        {
            "question": "Distribute flex items evenly with space between them.",
            "solution": "div { justify-content: space-between; }",
            "hint": "Use justify-content property.",
            "test": "justify-content: space-between" in code
        },
        {
            "question": "Align individual flex items to the end.",
            "solution": "div.item { align-self: flex-end; }",
            "hint": "Use align-self property.",
            "test": "align-self: flex-end" in code
        },
        {
            "question": "Make an item grow twice as much as others.",
            "solution": "div.item { flex-grow: 2; }",
            "hint": "Use flex-grow property.",
            "test": "flex-grow: 2" in code
        },
        {
            "question": "Prevent a flex item from shrinking.",
            "solution": "div.item { flex-shrink: 0; }",
            "hint": "Use flex-shrink property.",
            "test": "flex-shrink: 0" in code
        },
        {
            "question": "Set a flex item to have a base size of 100px.",
            "solution": "div.item { flex-basis: 100px; }",
            "hint": "Use flex-basis property.",
            "test": "flex-basis: 100px" in code
        },
        {
            "question": "Center flex items along both axes.",
            "solution": "div { justify-content: center; align-items: center; }",
            "hint": "Use justify-content and align-items.",
            "test": "justify-content: center" in code and "align-items: center" in code
        },
        {
            "question": "Reverse the order of flex items.",
            "solution": "div { flex-direction: row-reverse; }",
            "hint": "Use flex-direction property.",
            "test": "flex-direction: row-reverse" in code
        },
        {
            "question": "Space items evenly with equal gaps.",
            "solution": "div { justify-content: space-evenly; }",
            "hint": "Use justify-content property.",
            "test": "justify-content: space-evenly" in code
        },
        {
            "question": "Set flex-grow, flex-shrink, and flex-basis in a single line.",
            "solution": "div.item { flex: 1 1 50px; }",
            "hint": "Use the flex shorthand property.",
            "test": "flex: 1 1 50px" in code
        },
        {
            "question": "Align items at the center along the cross axis.",
            "solution": "div { align-items: center; }",
            "hint": "Use align-items property.",
            "test": "align-items: center" in code
        }
    ]
}
{
    "name": "Grid Layout",
    "description": "Learn about CSS Grid Layout and how to create responsive grid-based designs.",
    "puzzles": [
        {
            "question": "Create a grid container with 3 columns.",
            "solution": ".grid-container { display: grid; grid-template-columns: repeat(3, 1fr); }",
            "hint": "Use display grid and grid-template-columns.",
            "test": "display: grid" in code and "grid-template-columns" in code
        },
        {
            "question": "Set a grid container with 2 rows.",
            "solution": ".grid-container { display: grid; grid-template-rows: repeat(2, 100px); }",
            "hint": "Use grid-template-rows to define rows.",
            "test": "grid-template-rows" in code
        },
        {
            "question": "Set an element to span 2 columns.",
            "solution": ".grid-item { grid-column: span 2; }",
            "hint": "Use grid-column property.",
            "test": "grid-column" in code
        },
        {
            "question": "Align grid items to the center horizontally.",
            "solution": ".grid-container { display: grid; justify-items: center; }",
            "hint": "Use justify-items to align items horizontally.",
            "test": "justify-items: center" in code
        },
        {
            "question": "Align grid items to the center vertically.",
            "solution": ".grid-container { display: grid; align-items: center; }",
            "hint": "Use align-items property.",
            "test": "align-items: center" in code
        },
        {
            "question": "Set a grid item to start at column 2 and end at column 4.",
            "solution": ".grid-item { grid-column: 2 / 4; }",
            "hint": "Use grid-column with start and end values.",
            "test": "grid-column" in code
        },
        {
            "question": "Make a grid container with a 10px gap between items.",
            "solution": ".grid-container { display: grid; gap: 10px; }",
            "hint": "Use the gap property.",
            "test": "gap: 10px" in code
        },
        {
            "question": "Make a grid item occupy the entire row.",
            "solution": ".grid-item { grid-column: 1 / -1; }",
            "hint": "Use grid-column: 1 / -1 to stretch across all columns.",
            "test": "grid-column: 1 / -1" in code
        },
        {
            "question": "Set the grid container to have implicit rows with a minimum height of 100px.",
            "solution": ".grid-container { display: grid; grid-auto-rows: minmax(100px, auto); }",
            "hint": "Use grid-auto-rows property.",
            "test": "grid-auto-rows" in code
        },
        {
            "question": "Use fr units to make a grid with 2 columns, first twice the size of the second.",
            "solution": ".grid-container { display: grid; grid-template-columns: 2fr 1fr; }",
            "hint": "Use fr unit for flexible sizing.",
            "test": "grid-template-columns" in code
        },
        {
            "question": "Align the entire grid content to the center.",
            "solution": ".grid-container { display: grid; justify-content: center; align-content: center; }",
            "hint": "Use justify-content and align-content.",
            "test": "justify-content" in code and "align-content" in code
        },
        {
            "question": "Create a grid layout with areas named 'header', 'main', and 'footer'.",
            "solution": ".grid-container { display: grid; grid-template-areas: \"header\" \"main\" \"footer\"; }",
            "hint": "Use grid-template-areas.",
            "test": "grid-template-areas" in code
        },
        {
            "question": "Make a grid with columns of fixed, flexible, and auto width.",
            "solution": ".grid-container { display: grid; grid-template-columns: 200px 1fr auto; }",
            "hint": "Use a mix of px, fr, and auto for column sizes.",
            "test": "grid-template-columns" in code
        },
        {
            "question": "Set a grid container with an explicit column template and automatic row flow.",
            "solution": ".grid-container { display: grid; grid-template-columns: repeat(3, 1fr); grid-auto-rows: auto; }",
            "hint": "Use grid-template-columns and grid-auto-rows together.",
            "test": "grid-template-columns" in code and "grid-auto-rows" in code
        },
        {
            "question": "Set an element to start at row 2 and end at row 4.",
            "solution": ".grid-item { grid-row: 2 / 4; }",
            "hint": "Use grid-row property.",
            "test": "grid-row" in code
        }
    ]
}

{
    "name": "Positioning (Static, Relative, Absolute, Fixed, Sticky)",
    "description": "Learn about different CSS positioning methods: static, relative, absolute, fixed, and sticky.",
    "puzzles": [
        {
            "question": "Set an element to have static positioning.",
            "solution": "div { position: static; }",
            "hint": "Use position property with static.",
            "test": "position: static" in code
        },
        {
            "question": "Set an element to have relative positioning.",
            "solution": "div { position: relative; }",
            "hint": "Use position property with relative.",
            "test": "position: relative" in code
        },
        {
            "question": "Move an element 20px to the right from its normal position.",
            "solution": "div { position: relative; left: 20px; }",
            "hint": "Use position relative with left property.",
            "test": "left: 20px" in code
        },
        {
            "question": "Move an element 30px down from its normal position.",
            "solution": "div { position: relative; top: 30px; }",
            "hint": "Use position relative with top property.",
            "test": "top: 30px" in code
        },
        {
            "question": "Set an element to have absolute positioning.",
            "solution": "div { position: absolute; }",
            "hint": "Use position property with absolute.",
            "test": "position: absolute" in code
        },
        {
            "question": "Place an absolutely positioned element 50px from the top and 20px from the left.",
            "solution": "div { position: absolute; top: 50px; left: 20px; }",
            "hint": "Use absolute positioning with top and left.",
            "test": "top: 50px" in code and "left: 20px" in code
        },
        {
            "question": "Set an element to have fixed positioning.",
            "solution": "div { position: fixed; }",
            "hint": "Use position property with fixed.",
            "test": "position: fixed" in code
        },
        {
            "question": "Fix an element at the bottom-left of the screen.",
            "solution": "div { position: fixed; bottom: 0; left: 0; }",
            "hint": "Use position fixed with bottom and left properties.",
            "test": "bottom: 0" in code and "left: 0" in code
        },
        {
            "question": "Set an element to have sticky positioning.",
            "solution": "div { position: sticky; }",
            "hint": "Use position property with sticky.",
            "test": "position: sticky" in code
        },
        {
            "question": "Make an element stick to the top of the viewport when scrolling.",
            "solution": "div { position: sticky; top: 0; }",
            "hint": "Use position sticky with top property.",
            "test": "top: 0" in code
        },
        {
            "question": "Make an element positioned relative inside a container.",
            "solution": ".container { position: relative; }",
            "hint": "Use position relative inside the parent container.",
            "test": "position: relative" in code
        },
        {
            "question": "Make an absolutely positioned element center itself in a relative container.",
            "solution": ".container { position: relative; } .element { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }",
            "hint": "Use position absolute with transform property.",
            "test": "position: absolute" in code and "transform: translate(-50%, -50%)" in code
        },
        {
            "question": "Create a full-screen overlay using fixed positioning.",
            "solution": "div { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background-color: rgba(0,0,0,0.5); }",
            "hint": "Use position fixed with full viewport width and height.",
            "test": "width: 100vw" in code and "height: 100vh" in code
        },
        {
            "question": "Fix a navbar at the top of the page.",
            "solution": "nav { position: fixed; top: 0; width: 100%; background-color: #333; color: white; padding: 10px; }",
            "hint": "Use position fixed with top and full width.",
            "test": "position: fixed" in code and "top: 0" in code
        }
    ]
}
{
    "name": "Typography & Text Styling",
    "description": "Learn about CSS typography properties and text styling techniques.",
    "puzzles": [
        {
            "question": "Set the font size of a paragraph to 16 pixels.",
            "solution": "p { font-size: 16px; }",
            "hint": "Use the font-size property.",
            "test": "font-size" in code
        },
        {
            "question": "Make a heading text bold.",
            "solution": "h1 { font-weight: bold; }",
            "hint": "Use the font-weight property.",
            "test": "font-weight" in code
        },
        {
            "question": "Set the font family of a paragraph to Arial.",
            "solution": "p { font-family: Arial, sans-serif; }",
            "hint": "Use the font-family property.",
            "test": "font-family" in code
        },
        {
            "question": "Make a paragraph text italic.",
            "solution": "p { font-style: italic; }",
            "hint": "Use the font-style property.",
            "test": "font-style" in code
        },
        {
            "question": "Change the text color of a paragraph to blue.",
            "solution": "p { color: blue; }",
            "hint": "Use the color property.",
            "test": "color" in code
        },
        {
            "question": "Align the text of a paragraph to the center.",
            "solution": "p { text-align: center; }",
            "hint": "Use the text-align property.",
            "test": "text-align" in code
        },
        {
            "question": "Add an underline to a paragraph text.",
            "solution": "p { text-decoration: underline; }",
            "hint": "Use the text-decoration property.",
            "test": "text-decoration" in code
        },
        {
            "question": "Transform text to uppercase.",
            "solution": "p { text-transform: uppercase; }",
            "hint": "Use the text-transform property.",
            "test": "text-transform" in code
        },
        {
            "question": "Set the line height of a paragraph to 1.5.",
            "solution": "p { line-height: 1.5; }",
            "hint": "Use the line-height property.",
            "test": "line-height" in code
        },
        {
            "question": "Set the letter spacing of a paragraph to 2px.",
            "solution": "p { letter-spacing: 2px; }",
            "hint": "Use the letter-spacing property.",
            "test": "letter-spacing" in code
        },
        {
            "question": "Set the word spacing of a paragraph to 5px.",
            "solution": "p { word-spacing: 5px; }",
            "hint": "Use the word-spacing property.",
            "test": "word-spacing" in code
        },
        {
            "question": "Use a Google Font for the body text.",
            "solution": "body { font-family: 'Roboto', sans-serif; }",
            "hint": "Import a Google Font and use font-family.",
            "test": "font-family" in code
        },
        {
            "question": "Apply a text shadow to a heading.",
            "solution": "h1 { text-shadow: 2px 2px 5px gray; }",
            "hint": "Use the text-shadow property.",
            "test": "text-shadow" in code
        },
        {
            "question": "Make the text unselectable.",
            "solution": "p { user-select: none; }",
            "hint": "Use the user-select property.",
            "test": "user-select" in code
        },
        {
            "question": "Apply a gradient background to text.",
            "solution": "h1 { background: linear-gradient(to right, red, blue); -webkit-background-clip: text; color: transparent; }",
            "hint": "Use background-clip and color transparent.",
            "test": "background" in code and "-webkit-background-clip" in code
        }
    ]
}
{
    "name": "CSS Transitions & Animations",
    "description": "Learn about CSS transitions and animations for interactive effects.",
    "puzzles": [
        {
            "question": "Create a transition that changes the background color of a button when hovered.",
            "solution": "button { transition: background-color 0.5s ease; } button:hover { background-color: blue; }",
            "hint": "Use the transition property.",
            "test": "transition" in code
        },
        {
            "question": "Animate an element to move 100px to the right in 1 second.",
            "solution": "@keyframes moveRight { from { transform: translateX(0); } to { transform: translateX(100px); } } .box { animation: moveRight 1s linear; }",
            "hint": "Use @keyframes and animation property.",
            "test": "@keyframes" in code and "animation" in code
        },
        {
            "question": "Add a fade-in effect to a div over 2 seconds.",
            "solution": "@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } } .box { animation: fadeIn 2s ease-in; }",
            "hint": "Use opacity and @keyframes.",
            "test": "opacity" in code and "animation" in code
        },
        {
            "question": "Make an element scale up to 1.5 times its size when hovered.",
            "solution": "div { transition: transform 0.3s ease; } div:hover { transform: scale(1.5); }",
            "hint": "Use the transform property with scale.",
            "test": "transform" in code and "transition" in code
        },
        {
            "question": "Rotate an element 360 degrees continuously.",
            "solution": "@keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } } .box { animation: rotate 2s linear infinite; }",
            "hint": "Use rotate with infinite animation.",
            "test": "rotate" in code and "animation" in code
        },
        {
            "question": "Apply a bounce effect to an element.",
            "solution": "@keyframes bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-20px); } } .box { animation: bounce 1s ease-in-out infinite; }",
            "hint": "Use translateY for the bouncing effect.",
            "test": "translateY" in code and "animation" in code
        },
        {
            "question": "Create a hover effect that increases the width of a div.",
            "solution": "div { transition: width 0.4s ease; } div:hover { width: 200px; }",
            "hint": "Use width with transition.",
            "test": "width" in code and "transition" in code
        },
        {
            "question": "Make text color transition smoothly over 1 second.",
            "solution": "p { transition: color 1s ease-in-out; } p:hover { color: red; }",
            "hint": "Use color with transition.",
            "test": "color" in code and "transition" in code
        },
        {
            "question": "Create a keyframe animation that pulses an element.",
            "solution": "@keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.2); } } .box { animation: pulse 1s ease-in-out infinite; }",
            "hint": "Use scale with keyframes.",
            "test": "scale" in code and "animation" in code
        },
        {
            "question": "Add a delay before an animation starts.",
            "solution": "div { animation: fadeIn 2s ease-in 1s; }",
            "hint": "Use animation-delay property.",
            "test": "animation-delay" in code
        },
        {
            "question": "Make an element fade out on hover.",
            "solution": "div { transition: opacity 0.5s ease; } div:hover { opacity: 0; }",
            "hint": "Use opacity with transition.",
            "test": "opacity" in code and "transition" in code
        },
        {
            "question": "Create a slide-in effect from the left.",
            "solution": "@keyframes slideIn { from { transform: translateX(-100%); } to { transform: translateX(0); } } .box { animation: slideIn 1s ease-out; }",
            "hint": "Use translateX with keyframes.",
            "test": "translateX" in code and "animation" in code
        },
        {
            "question": "Make a button shrink when clicked.",
            "solution": "button { transition: transform 0.2s ease; } button:active { transform: scale(0.8); }",
            "hint": "Use scale with transition.",
            "test": "scale" in code and "transition" in code
        },
        {
            "question": "Create a background color animation effect.",
            "solution": "@keyframes bgColorChange { 0% { background-color: red; } 50% { background-color: yellow; } 100% { background-color: green; } } .box { animation: bgColorChange 3s linear infinite; }",
            "hint": "Use background-color with keyframes.",
            "test": "background-color" in code and "animation" in code
        },
        {
            "question": "Add a blinking text effect.",
            "solution": "@keyframes blink { 50% { opacity: 0; } } .text { animation: blink 1s step-start infinite; }",
            "hint": "Use opacity and step-start.",
            "test": "opacity" in code and "animation" in code
        }
    ]
}
{
    "name": "Responsive Design & Media Queries",
    "description": "Learn about responsive design techniques and media queries for adaptive layouts.",
    "puzzles": [
        {
            "question": "Create a media query that changes the background color to blue when the screen width is less than 600px.",
            "solution": "@media (max-width: 600px) { body { background-color: blue; } }",
            "hint": "Use max-width in the media query.",
            "test": "@media" in code and "max-width" in code
        },
        {
            "question": "Make an image responsive using CSS.",
            "solution": "img { max-width: 100%; height: auto; }",
            "hint": "Use max-width and height properties.",
            "test": "max-width" in code and "height" in code
        },
        {
            "question": "Hide an element when the screen width is less than 500px.",
            "solution": "@media (max-width: 500px) { .hide { display: none; } }",
            "hint": "Use display: none inside the media query.",
            "test": "display" in code and "none" in code
        },
        {
            "question": "Change text size for smaller screens (less than 768px).",
            "solution": "@media (max-width: 768px) { p { font-size: 14px; } }",
            "hint": "Modify font-size inside a media query.",
            "test": "font-size" in code and "@media" in code
        },
        {
            "question": "Create a flexible grid layout with media queries.",
            "solution": "@media (max-width: 800px) { .container { display: flex; flex-direction: column; } }",
            "hint": "Use flex-direction for responsive layout.",
            "test": "flex-direction" in code and "@media" in code
        },
        {
            "question": "Apply different padding for screens larger than 1024px.",
            "solution": "@media (min-width: 1024px) { .box { padding: 20px; } }",
            "hint": "Use min-width to target larger screens.",
            "test": "padding" in code and "min-width" in code
        },
        {
            "question": "Use viewport units for a full-width section.",
            "solution": ".section { width: 100vw; height: 50vh; }",
            "hint": "Use vw and vh units for responsive sizing.",
            "test": "vw" in code and "vh" in code
        },
        {
            "question": "Center an element horizontally and vertically responsively.",
            "solution": ".center { display: flex; justify-content: center; align-items: center; height: 100vh; }",
            "hint": "Use flexbox properties for centering.",
            "test": "justify-content" in code and "align-items" in code
        },
        {
            "question": "Create a responsive navigation menu.",
            "solution": "@media (max-width: 768px) { .menu { display: none; } .menu-icon { display: block; } }",
            "hint": "Use media queries to hide/show menu elements.",
            "test": "display" in code and "@media" in code
        },
        {
            "question": "Change font-weight for smaller screens.",
            "solution": "@media (max-width: 600px) { h1 { font-weight: normal; } }",
            "hint": "Modify font-weight inside media queries.",
            "test": "font-weight" in code and "@media" in code
        },
        {
            "question": "Apply different border styles based on screen size.",
            "solution": "@media (max-width: 700px) { div { border: 1px solid red; } } @media (min-width: 701px) { div { border: 2px dashed blue; } }",
            "hint": "Use multiple media queries for different styles.",
            "test": "border" in code and "@media" in code
        },
        {
            "question": "Use CSS grid for a responsive layout.",
            "solution": ".grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); }",
            "hint": "Use auto-fit and minmax for flexible grids.",
            "test": "grid-template-columns" in code and "grid" in code
        },
        {
            "question": "Change flex-wrap based on screen width.",
            "solution": "@media (max-width: 600px) { .flex-container { flex-wrap: wrap; } }",
            "hint": "Modify flex-wrap inside media queries.",
            "test": "flex-wrap" in code and "@media" in code
        },
        {
            "question": "Apply a box-shadow effect only on larger screens.",
            "solution": "@media (min-width: 800px) { .card { box-shadow: 5px 5px 10px gray; } }",
            "hint": "Use box-shadow property in a media query.",
            "test": "box-shadow" in code and "@media" in code
        },
        {
            "question": "Make a footer stick to the bottom on all screen sizes.",
            "solution": "footer { position: fixed; bottom: 0; width: 100%; }",
            "hint": "Use position: fixed for a sticky footer.",
            "test": "position" in code and "bottom" in code
        }
    ]
}
{
    "name": "Pseudo-classes & Pseudo-elements",
    "description": "Learn about CSS pseudo-classes and pseudo-elements for styling specific parts of elements.",
    "puzzles": [
        {
            "question": "Change the background color of a button when hovered.",
            "solution": "button:hover { background-color: blue; }",
            "hint": "Use the :hover pseudo-class.",
            "test": ":hover" in code and "background-color" in code
        },
        {
            "question": "Style the first letter of a paragraph to be larger.",
            "solution": "p::first-letter { font-size: 2em; }",
            "hint": "Use the ::first-letter pseudo-element.",
            "test": "::first-letter" in code and "font-size" in code
        },
        {
            "question": "Change the color of visited links.",
            "solution": "a:visited { color: purple; }",
            "hint": "Use the :visited pseudo-class.",
            "test": ":visited" in code and "color" in code
        },
        {
            "question": "Style the placeholder text inside an input field.",
            "solution": "input::placeholder { color: gray; }",
            "hint": "Use the ::placeholder pseudo-element.",
            "test": "::placeholder" in code and "color" in code
        },
        {
            "question": "Apply a border to an input field when it is focused.",
            "solution": "input:focus { border: 2px solid red; }",
            "hint": "Use the :focus pseudo-class.",
            "test": ":focus" in code and "border" in code
        },
        {
            "question": "Make every even table row have a light gray background.",
            "solution": "tr:nth-child(even) { background-color: lightgray; }",
            "hint": "Use the :nth-child pseudo-class.",
            "test": ":nth-child" in code and "background-color" in code
        },
        {
            "question": "Underline links only when hovered.",
            "solution": "a:hover { text-decoration: underline; }",
            "hint": "Use the :hover pseudo-class.",
            "test": ":hover" in code and "text-decoration" in code
        },
        {
            "question": "Change the text color of the first line of a paragraph.",
            "solution": "p::first-line { color: red; }",
            "hint": "Use the ::first-line pseudo-element.",
            "test": "::first-line" in code and "color" in code
        },
        {
            "question": "Apply a box shadow to an element when it is active.",
            "solution": "button:active { box-shadow: 2px 2px 5px gray; }",
            "hint": "Use the :active pseudo-class.",
            "test": ":active" in code and "box-shadow" in code
        },
        {
            "question": "Style the first child of a list to have bold text.",
            "solution": "li:first-child { font-weight: bold; }",
            "hint": "Use the :first-child pseudo-class.",
            "test": ":first-child" in code and "font-weight" in code
        },
        {
            "question": "Make only the last paragraph in a container italic.",
            "solution": "p:last-child { font-style: italic; }",
            "hint": "Use the :last-child pseudo-class.",
            "test": ":last-child" in code and "font-style" in code
        },
        {
            "question": "Style the first letter of blockquotes with a different font size.",
            "solution": "blockquote::first-letter { font-size: 1.5em; }",
            "hint": "Use the ::first-letter pseudo-element.",
            "test": "::first-letter" in code and "font-size" in code
        },
        {
            "question": "Apply a different color to input fields that are required.",
            "solution": "input:required { border-color: red; }",
            "hint": "Use the :required pseudo-class.",
            "test": ":required" in code and "border-color" in code
        },
        {
            "question": "Make a div appear only when hovered over its parent.",
            "solution": ".parent:hover .child { display: block; }",
            "hint": "Use the :hover pseudo-class on the parent.",
            "test": ":hover" in code and "display" in code
        },
        {
            "question": "Apply a special styling to a disabled button.",
            "solution": "button:disabled { background-color: gray; cursor: not-allowed; }",
            "hint": "Use the :disabled pseudo-class.",
            "test": ":disabled" in code and "background-color" in code
        }
    ]
}
{
    "name": "CSS Variables & Custom Properties",
    "description": "Learn about CSS variables and how to use custom properties for reusable styles.",
    "puzzles": [
        {
            "question": "Define a CSS variable for the primary color and use it for the background.",
            "solution": ":root { --primary-color: blue; }\nbody { background-color: var(--primary-color); }",
            "hint": "Use :root to define variables and var() to use them.",
            "test": "--primary-color" in code and "var(--primary-color)" in code
        },
        {
            "question": "Create a button with a dynamic text color using a CSS variable.",
            "solution": ":root { --text-color: white; }\nbutton { color: var(--text-color); }",
            "hint": "Use var() to access the variable.",
            "test": "--text-color" in code and "var(--text-color)" in code
        },
        {
            "question": "Adjust padding globally using a CSS variable.",
            "solution": ":root { --padding-size: 10px; }\ndiv { padding: var(--padding-size); }",
            "hint": "Define a variable and apply it to the padding property.",
            "test": "--padding-size" in code and "var(--padding-size)" in code
        },
        {
            "question": "Modify border radius using a CSS variable.",
            "solution": ":root { --border-radius: 5px; }\n.box { border-radius: var(--border-radius); }",
            "hint": "Use var() to apply a border-radius variable.",
            "test": "--border-radius" in code and "var(--border-radius)" in code
        },
        {
            "question": "Create a theme switcher using CSS variables.",
            "solution": ":root { --bg-color: white; }\n.dark-mode { --bg-color: black; }\nbody { background-color: var(--bg-color); }",
            "hint": "Define a variable in :root and override it in a class.",
            "test": "--bg-color" in code and "var(--bg-color)" in code
        },
        {
            "question": "Apply different font sizes using CSS variables.",
            "solution": ":root { --font-size: 16px; }\np { font-size: var(--font-size); }",
            "hint": "Define font size in a variable and use var().",
            "test": "--font-size" in code and "var(--font-size)" in code
        },
        {
            "question": "Use a CSS variable to control margin spacing.",
            "solution": ":root { --margin-size: 15px; }\ndiv { margin: var(--margin-size); }",
            "hint": "Set a variable for margin and apply it with var().",
            "test": "--margin-size" in code and "var(--margin-size)" in code
        },
        {
            "question": "Set a default transition duration using a CSS variable.",
            "solution": ":root { --transition-time: 0.3s; }\nbutton { transition: all var(--transition-time); }",
            "hint": "Define a variable and apply it in transition property.",
            "test": "--transition-time" in code and "var(--transition-time)" in code
        },
        {
            "question": "Create a reusable shadow effect with a CSS variable.",
            "solution": ":root { --box-shadow: 2px 2px 10px gray; }\ndiv { box-shadow: var(--box-shadow); }",
            "hint": "Define a shadow variable and apply it.",
            "test": "--box-shadow" in code and "var(--box-shadow)" in code
        },
        {
            "question": "Change text color dynamically using a CSS variable.",
            "solution": ":root { --text-color: black; }\nh1 { color: var(--text-color); }",
            "hint": "Use var() to access the variable.",
            "test": "--text-color" in code and "var(--text-color)" in code
        },
        {
            "question": "Define and use multiple CSS variables in a single selector.",
            "solution": ":root { --padding: 20px; --bg-color: lightgray; }\nsection { padding: var(--padding); background-color: var(--bg-color); }",
            "hint": "Use multiple var() calls inside the selector.",
            "test": "--padding" in code and "--bg-color" in code
        },
        {
            "question": "Control button hover effects with CSS variables.",
            "solution": ":root { --hover-color: green; }\nbutton:hover { background-color: var(--hover-color); }",
            "hint": "Use var() inside a :hover selector.",
            "test": "--hover-color" in code and "var(--hover-color)" in code
        },
        {
            "question": "Use a CSS variable for width and height.",
            "solution": ":root { --size: 100px; }\ndiv { width: var(--size); height: var(--size); }",
            "hint": "Define --size and use it for both width and height.",
            "test": "--size" in code and "var(--size)" in code
        },
        {
            "question": "Define global spacing variables and apply them.",
            "solution": ":root { --spacing: 10px; }\np { margin-bottom: var(--spacing); }",
            "hint": "Use a variable for spacing-related styles.",
            "test": "--spacing" in code and "var(--spacing)" in code
        },
        {
            "question": "Override a CSS variable inside a class.",
            "solution": ":root { --color: blue; }\n.alert { --color: red; }\np { color: var(--color); }",
            "hint": "Override the variable within a specific class.",
            "test": "--color" in code and "var(--color)" in code
        }
    ]
}
{
    "name": "Z-Index & Stacking Context",
    "description": "Learn about CSS z-index and stacking context to control element layering.",
    "puzzles": [
        {
            "question": "Set a z-index value for a header element to place it above other elements.",
            "solution": "header { z-index: 10; position: relative; }",
            "hint": "Use a positive z-index value and ensure position is set.",
            "test": "z-index" in code and "position" in code
        },
        {
            "question": "Make an element always stay on top using z-index.",
            "solution": ".sticky-element { z-index: 9999; position: fixed; }",
            "hint": "Use a very high z-index with position: fixed.",
            "test": "z-index" in code and "position: fixed" in code
        },
        {
            "question": "Create an overlapping effect with multiple divs.",
            "solution": ".box1 { z-index: 2; position: absolute; } .box2 { z-index: 1; position: absolute; }",
            "hint": "Use different z-index values with absolute positioning.",
            "test": "z-index" in code and "position: absolute" in code
        },
        {
            "question": "Ensure a modal appears above all other content.",
            "solution": ".modal { z-index: 1000; position: fixed; }",
            "hint": "Use a high z-index value with fixed positioning.",
            "test": "z-index" in code and "position: fixed" in code
        },
        {
            "question": "Place a tooltip above its parent element.",
            "solution": ".tooltip { z-index: 5; position: absolute; }",
            "hint": "Set a higher z-index than the parent.",
            "test": "z-index" in code and "position: absolute" in code
        },
        {
            "question": "Make an element appear below another element using z-index.",
            "solution": ".background { z-index: -1; position: relative; }",
            "hint": "Use a negative z-index value with a relative position.",
            "test": "z-index" in code and "position: relative" in code
        },
        {
            "question": "Use z-index with flexbox to layer items correctly.",
            "solution": ".flex-item { z-index: 3; position: relative; }",
            "hint": "Ensure position is set along with z-index.",
            "test": "z-index" in code and "position: relative" in code
        },
        {
            "question": "Prevent a child element from breaking the stacking context of its parent.",
            "solution": ".parent { position: relative; z-index: 10; } .child { z-index: 5; position: absolute; }",
            "hint": "Ensure the parent has a defined z-index and position.",
            "test": "z-index" in code and "position" in code
        },
        {
            "question": "Stack multiple elements in descending order.",
            "solution": ".first { z-index: 3; } .second { z-index: 2; } .third { z-index: 1; }",
            "hint": "Assign decreasing z-index values.",
            "test": "z-index" in code
        },
        {
            "question": "Use z-index to create a layered card effect.",
            "solution": ".card { z-index: 1; position: relative; } .card:hover { z-index: 5; }",
            "hint": "Increase z-index on hover.",
            "test": "z-index" in code and "hover" in code
        },
        {
            "question": "Fix a navigation bar at the top with z-index.",
            "solution": ".navbar { z-index: 100; position: fixed; top: 0; }",
            "hint": "Use a high z-index with fixed positioning.",
            "test": "z-index" in code and "position: fixed" in code
        },
        {
            "question": "Ensure an image appears behind text using z-index.",
            "solution": "img { z-index: -1; position: absolute; }",
            "hint": "Use a negative z-index value with absolute positioning.",
            "test": "z-index" in code and "position: absolute" in code
        },
        {
            "question": "Set a sidebar to be always on top of other content.",
            "solution": ".sidebar { z-index: 50; position: fixed; }",
            "hint": "Use a high z-index with fixed positioning.",
            "test": "z-index" in code and "position: fixed" in code
        },
        {
            "question": "Use z-index to prevent an element from overlapping another.",
            "solution": ".content { z-index: 10; } .footer { z-index: 5; }",
            "hint": "Ensure the lower element has a smaller z-index.",
            "test": "z-index" in code
        },
        {
            "question": "Create a stacking context using opacity.",
            "solution": ".container { opacity: 0.99; position: relative; z-index: 1; }",
            "hint": "Use opacity to trigger a new stacking context.",
            "test": "opacity" in code and "z-index" in code
        }
    ]
}
{
    "name": "CSS Filters & Blend Modes",
    "description": "Learn about CSS filters and blend modes to enhance visual effects.",
    "puzzles": [
        {
            "question": "Apply a grayscale filter to an image.",
            "solution": "img { filter: grayscale(100%); }",
            "hint": "Use the 'filter' property with 'grayscale'.",
            "test": "filter" in code and "grayscale" in code
        },
        {
            "question": "Apply a blur effect to a div element.",
            "solution": ".blur-box { filter: blur(5px); }",
            "hint": "Use 'filter' with 'blur' and a pixel value.",
            "test": "filter" in code and "blur" in code
        },
        {
            "question": "Increase the brightness of an image.",
            "solution": "img { filter: brightness(150%); }",
            "hint": "Use 'brightness' with a percentage value.",
            "test": "filter" in code and "brightness" in code
        },
        {
            "question": "Apply a sepia effect to a background image.",
            "solution": "div { filter: sepia(80%); }",
            "hint": "Use 'filter' with 'sepia'.",
            "test": "filter" in code and "sepia" in code
        },
        {
            "question": "Make an image appear inverted.",
            "solution": "img { filter: invert(100%); }",
            "hint": "Use 'invert' with 100%.",
            "test": "filter" in code and "invert" in code
        },
        {
            "question": "Apply a hue rotation effect to an element.",
            "solution": "div { filter: hue-rotate(90deg); }",
            "hint": "Use 'hue-rotate' with a degree value.",
            "test": "filter" in code and "hue-rotate" in code
        },
        {
            "question": "Combine multiple filters for an image.",
            "solution": "img { filter: brightness(120%) contrast(110%) blur(2px); }",
            "hint": "Use multiple filter functions together.",
            "test": "filter" in code and "contrast" in code
        },
        {
            "question": "Apply a multiply blend mode to an image.",
            "solution": "img { mix-blend-mode: multiply; }",
            "hint": "Use 'mix-blend-mode' with 'multiply'.",
            "test": "mix-blend-mode" in code and "multiply" in code
        },
        {
            "question": "Make text appear with an overlay blend effect.",
            "solution": "h1 { mix-blend-mode: overlay; }",
            "hint": "Use 'overlay' as the blend mode.",
            "test": "mix-blend-mode" in code and "overlay" in code
        },
        {
            "question": "Apply a darken blend mode to a div background.",
            "solution": "div { mix-blend-mode: darken; }",
            "hint": "Use 'darken' as the blend mode.",
            "test": "mix-blend-mode" in code and "darken" in code
        },
        {
            "question": "Apply a soft light blend mode to an image.",
            "solution": "img { mix-blend-mode: soft-light; }",
            "hint": "Use 'soft-light' as the blend mode.",
            "test": "mix-blend-mode" in code and "soft-light" in code
        },
        {
            "question": "Make an element’s background blend with the one behind it.",
            "solution": "div { background-blend-mode: screen; }",
            "hint": "Use 'background-blend-mode'.",
            "test": "background-blend-mode" in code and "screen" in code
        },
        {
            "question": "Apply a difference blend mode to a heading.",
            "solution": "h2 { mix-blend-mode: difference; }",
            "hint": "Use 'difference' as the blend mode.",
            "test": "mix-blend-mode" in code and "difference" in code
        },
        {
            "question": "Use a color-dodge blend mode on an image.",
            "solution": "img { mix-blend-mode: color-dodge; }",
            "hint": "Use 'color-dodge' as the blend mode.",
            "test": "mix-blend-mode" in code and "color-dodge" in code
        },
        {
            "question": "Enhance contrast using a contrast filter.",
            "solution": "img { filter: contrast(200%); }",
            "hint": "Use 'contrast' with a percentage value.",
            "test": "filter" in code and "contrast" in code
        }
    ]
}
{
    "name": "CSS Shapes & Clip Paths",
    "description": "Learn about CSS shapes and clip-paths to create unique design elements.",
    "puzzles": [
        {
            "question": "Create a circular div using clip-path.",
            "solution": ".circle { clip-path: circle(50%); }",
            "hint": "Use 'clip-path' with 'circle()'.",
            "test": "clip-path" in code and "circle" in code
        },
        {
            "question": "Clip an image into a polygon shape.",
            "solution": "img { clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%); }",
            "hint": "Use 'clip-path' with 'polygon()'.",
            "test": "clip-path" in code and "polygon" in code
        },
        {
            "question": "Apply an ellipse clip path to a div.",
            "solution": "div { clip-path: ellipse(40% 60% at 50% 50%); }",
            "hint": "Use 'clip-path' with 'ellipse()'.",
            "test": "clip-path" in code and "ellipse" in code
        },
        {
            "question": "Use inset clip path to crop an element.",
            "solution": "div { clip-path: inset(10px 20px 30px 40px); }",
            "hint": "Use 'clip-path' with 'inset()'.",
            "test": "clip-path" in code and "inset" in code
        },
        {
            "question": "Create a star-shaped clip path.",
            "solution": "div { clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%); }",
            "hint": "Use 'polygon()' to create the star shape.",
            "test": "clip-path" in code and "polygon" in code
        },
        {
            "question": "Apply a triangle clip path to an image.",
            "solution": "img { clip-path: polygon(50% 0%, 100% 100%, 0% 100%); }",
            "hint": "Use 'clip-path' with a three-point polygon.",
            "test": "clip-path" in code and "polygon" in code
        },
        {
            "question": "Clip a div into a heart shape.",
            "solution": "div { clip-path: path('M50,15 C30,-10 0,10 10,40 C0,80 50,90 50,100 C50,90 100,80 90,40 C100,10 70,-10 50,15'); }",
            "hint": "Use 'clip-path' with 'path()'.",
            "test": "clip-path" in code and "path" in code
        },
        {
            "question": "Create a hexagonal shape using clip-path.",
            "solution": "div { clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); }",
            "hint": "Use 'polygon()' to define six points.",
            "test": "clip-path" in code and "polygon" in code
        },
        {
            "question": "Use CSS shape-outside to wrap text around a circular shape.",
            "solution": ".text-wrap { shape-outside: circle(50%); float: left; width: 200px; height: 200px; }",
            "hint": "Use 'shape-outside' and 'float'.",
            "test": "shape-outside" in code and "circle" in code
        },
        {
            "question": "Create a text wrapping effect using shape-outside with an ellipse.",
            "solution": ".text-wrap { shape-outside: ellipse(40% 60%); float: right; }",
            "hint": "Use 'shape-outside' with 'ellipse()'.",
            "test": "shape-outside" in code and "ellipse" in code
        },
        {
            "question": "Apply shape-outside with a polygon for text wrapping.",
            "solution": ".text-wrap { shape-outside: polygon(0% 50%, 50% 0%, 100% 50%, 50% 100%); }",
            "hint": "Use 'shape-outside' with 'polygon()'.",
            "test": "shape-outside" in code and "polygon" in code
        },
        {
            "question": "Use shape-margin to adjust text spacing around a shape.",
            "solution": ".text-wrap { shape-margin: 10px; shape-outside: circle(50%); }",
            "hint": "Use 'shape-margin' to add space around the shape.",
            "test": "shape-margin" in code
        },
        {
            "question": "Clip an element using an SVG path.",
            "solution": "div { clip-path: url(#myPath); }",
            "hint": "Define an SVG path and use 'clip-path' with 'url()'.",
            "test": "clip-path" in code and "url" in code
        },
        {
            "question": "Create a wave-shaped clip path effect.",
            "solution": "div { clip-path: polygon(0% 50%, 20% 40%, 40% 60%, 60% 40%, 80% 60%, 100% 50%, 100% 100%, 0% 100%); }",
            "hint": "Use 'polygon()' to create a wave shape.",
            "test": "clip-path" in code and "polygon" in code
        },
        {
            "question": "Apply a complex SVG-defined clip path to an element.",
            "solution": "div { clip-path: url(#complexShape); }",
            "hint": "Use an SVG-defined clip path with 'url()'.",
            "test": "clip-path" in code and "url" in code
        }
    ]
}
{
    "name": "CSS Frameworks & Preprocessors (SASS, LESS)",
    "description": "Learn about CSS frameworks and preprocessors like SASS and LESS.",
    "puzzles": [
        {
            "question": "Define a SASS variable for primary color.",
            "solution": "$primary-color: #3498db;",
            "hint": "Use the '$' symbol to define a variable in SASS.",
            "test": "$primary-color" in code
        },
        {
            "question": "Nest a CSS rule inside another using SASS.",
            "solution": ".parent {\n  .child {\n    color: red;\n  }\n}",
            "hint": "Use indentation to nest CSS selectors.",
            "test": ".parent" in code and ".child" in code
        },
        {
            "question": "Extend an existing class in SASS.",
            "solution": ".button {\n  padding: 10px;\n}\n.primary {\n  @extend .button;\n  background-color: blue;\n}",
            "hint": "Use '@extend' to inherit styles.",
            "test": "@extend" in code
        },
        {
            "question": "Create a mixin for rounded corners in SASS.",
            "solution": "@mixin rounded($radius) {\n  border-radius: $radius;\n}\n.box {\n  @include rounded(10px);\n}",
            "hint": "Use '@mixin' to define reusable styles.",
            "test": "@mixin" in code and "@include" in code
        },
        {
            "question": "Compile a LESS file into CSS.",
            "solution": "lessc styles.less styles.css",
            "hint": "Use the 'lessc' command to compile LESS files.",
            "test": "lessc" in code
        },
        {
            "question": "Define a variable in LESS.",
            "solution": "@primary-color: #3498db;",
            "hint": "Use '@' to define a variable in LESS.",
            "test": "@primary-color" in code
        },
        {
            "question": "Create a mixin for box shadows in LESS.",
            "solution": ".box-shadow(@x, @y, @blur, @color) {\n  box-shadow: @x @y @blur @color;\n}\n.card {\n  .box-shadow(2px, 2px, 5px, #888);\n}",
            "hint": "Define a reusable mixin in LESS using parameters.",
            "test": ".box-shadow" in code
        },
        {
            "question": "Use an if-else condition in SASS.",
            "solution": "@if lightness($primary-color) > 50% {\n  background: black;\n} @else {\n  background: white;\n}",
            "hint": "Use '@if' and '@else' for conditional styling.",
            "test": "@if" in code
        },
        {
            "question": "Use loops in SASS to generate classes dynamically.",
            "solution": "@for $i from 1 through 3 {\n  .col-#{$i} {\n    width: 100% / $i;\n  }\n}",
            "hint": "Use '@for' to iterate through a range of values.",
            "test": "@for" in code
        },
        {
            "question": "Import a SASS file into another file.",
            "solution": "@import 'variables';",
            "hint": "Use '@import' to include another SASS file.",
            "test": "@import" in code
        },
        {
            "question": "Define a function in SASS to lighten a color.",
            "solution": "@function lighten-color($color, $amount) {\n  @return lighten($color, $amount);\n}",
            "hint": "Use '@function' to create reusable functions in SASS.",
            "test": "@function" in code
        },
        {
            "question": "Use nesting in LESS to style child elements.",
            "solution": ".menu {\n  ul {\n    li {\n      color: blue;\n    }\n  }\n}",
            "hint": "LESS supports nesting similar to SASS.",
            "test": ".menu" in code and "ul" in code
        },
        {
            "question": "Use 'darken' function in LESS to modify color shade.",
            "solution": "color: darken(@primary-color, 10%);",
            "hint": "Use 'darken()' to reduce brightness.",
            "test": "darken" in code
        },
        {
            "question": "Use math operations in LESS.",
            "solution": "width: (100% / 3);",
            "hint": "Use arithmetic operations directly in LESS properties.",
            "test": "/ 3" in code
        },
        {
            "question": "Extend a class in LESS.",
            "solution": ".btn {\n  padding: 10px;\n}\n.primary {\n  &:extend(.btn);\n  background: blue;\n}",
            "hint": "Use '&:extend()' to inherit styles in LESS.",
            "test": "&:extend" in code
        }
    ]
}
