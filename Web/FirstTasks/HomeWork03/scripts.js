
let test = prompt("Как Вас зовут?","Имя");
showMessage( test );

function showMessage(userName) {
    let message = 'Привет, ' + userName;
    alert(message);
}
