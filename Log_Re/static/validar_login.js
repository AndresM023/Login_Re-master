const clave1 = document.getElementById('contraseña3');
const clave2 = document.getElementById('nuevaclave');
const clave3 = document.getElementById('newp2')

    toggleBtn.onclick = function (){
        if (clave1.type === 'password') {
            clave1.setAttribute('type', 'text');
            toggleBtn.classList.add('hide');
        }
        else {
            clave1.setAttribute('type', 'password');
            toggleBtn.classList.remove('hide');

        }
    };

     toggleBtn1.onclick = function (){
        if (clave2.type === 'password') {
            clave2.setAttribute('type', 'text');
            toggleBtn1.classList.add('mostrar');
        }
        else {
            clave2.setAttribute('type', 'password');
            toggleBtn1.classList.remove('mostrar');

        }
    };


    toggleBtn.onclick = function (){
        if (clave3.type === 'password') {
            clave3.setAttribute('type', 'text');
            toggleBtn.classList.add('hide');
        }
        else {
            clave3.setAttribute('type', 'password');
            toggleBtn.classList.remove('hide');

        }
    };

