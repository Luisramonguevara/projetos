document.addEventListener('DOMContentLoaded', function() {
 
    const display = document.getElementById('display');
 
    const buttons = document.querySelectorAll('.btn');
 
    let currentInput = '0';
    let operator = null;
    let previousInput = null;
    let expression = '';
 
 
buttons.forEach(button => {
    button.addEventListener('click', () => {
 
        const buttonText = button.textContent;
 
        if (button.id === 'c') {
 
            currentInput = '0';
            operator = null;
            previousInput = null;
            expression = '';
            display.value = currentInput;
           
        }else if (button.id === 'ce') {
            currentInput = '0';
            display.value = currentInput;
 
        }else if (button.id === 'backspace') {
            currentInput = currentInput.slice(0, -1) || '0';
            display.value = currentInput;
 
        }else if (button.id === 'equals') {
            if(operator && previousInput !== null) {
                currentInput = calculate(parseFloat(previousInput), operator);
                operator = null;
                previousInput = null;
                expression = currentInput;
                display.value = currentInput;

            }else {
                previousInput = currentInput;
                operator = buttonText;
                expression += ' ' + currentInput + ' ' + operator;
                display.value = expression;
                currentInput = '0';
            
 
            }
        }else {
            if (currentInput === "0") {
                currentInput = buttonText;
            } else {
                currentInput += buttonText;
            }
            display.value = currentInput;
            expression += button;
        }
 
    });
});

function resultado() {
    var result = "";
    for (var i=0;i<Array.length;i++) {
        result += Array[i];
}

    result = eval(result);
    txt.innerHTML = result;
    display.value = result;
    currentInput = "0"
    expression = "";
            
    
}
 
 
 
});


