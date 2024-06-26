let currentInput = '0';

function appendToDisplay(value) {
    if (currentInput === '0') {
        currentInput = '';
    }
    document.getElementById('display').value += value;
}

function clearDisplay() {
    document.getElementById('display').value = '';
    currentInput = '0';
}

function calculate() {
    let displayValue = document.getElementById('display').value;
    let result;
    try {
        result = eval(displayValue);
        document.getElementById('display').value = result;
    } catch (error) {
        document.getElementById('display').value = 'Error';
    }
    currentInput = result.toString();
}
