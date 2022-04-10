form = document.getElementById('Form')
add = document.getElementById('Adicionar')
inputName = document.getElementById('Nome')
add.addEventListener('click',()=>{
    if (inputName.value)
    {
       form.innerHTML+=`<input name="${inputName.value}" value="${inputName.value}">`
       inputName.value=''
    }
    else
    {
        alert('Nome Invalido!')
    }
})