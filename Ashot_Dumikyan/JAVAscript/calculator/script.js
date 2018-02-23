var textField = document.getElementById('textField');

textField.focus();

var submit = document.getElementById('submitButton');

submit.addEventListener('click', buttonClicked, false);

function buttonClicked(e) {

e.preventDefault();

x = textField.value;

try {

x = eval(x);

textField.value = x;

} catch (ex) {

alert('Неверный формат');

}

}

function addToField(n) {

textField.value += n;

textField.focus();

}

function power(y) {

x = textField.value;

x = Math.pow(x, y);

textField.value = x;

textField.focus();

}

function powten() {

x = textField.value;

x = Math.pow(10, x);

textField.value = x;

textField.focus();

}