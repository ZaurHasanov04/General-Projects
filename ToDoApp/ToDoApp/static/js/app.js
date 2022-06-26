
let edit = document.querySelector('.edit')

let buttons = document.querySelectorAll('.actions')

let forms = document.querySelectorAll('#myform')

forms.forEach(function(f){
    f.nextElementSibling.childNodes[3].addEventListener('click', () =>{
        f.submit()
    })
})


buttons.forEach(function(link){

    link.addEventListener('click', () =>{
        
        let accept = link.childNodes[3]
        link.childNodes[1].style.display='none'
        accept.style.display='inline-block'
    
        let item_input = link.previousElementSibling[1]
    
        item_input.removeAttribute('readonly')
        item_input.focus()
    })
})


