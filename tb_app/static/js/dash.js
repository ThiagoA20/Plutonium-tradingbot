buildList()

function buildList(){
    let wrapper = document.getElementById('list-wrapper')

    let url = 'http://127.0.0.1:8000/api/listdeals/'

    fetch(url)
    .then((resp) => resp.json())
    .then(function(data){
        console.log('Data:', data)

        let list = data
        for (let i in list) {
            let item = `
                <div id="data-row-${i}" class="task-wrapper flex-wrapper">
                    <div style='flex:7'>
                        <span class='title'>${list[i].title}</span>
                        <span>Op:${list[i].operation}</span>
                        <span>Indicador: ${list[i].indicators}</span>
                        <span>Contribuitors: ${list[i].contribuitors}</span>
                        <span>Amount: ${list[i].amount}</span>
                        <span>Creation: ${list[i].creation}</span>
                    </div>
                    <div>
                        <span>Ativo: ${list[i].investment}</span>
                        <span>Estratégia: ${list[i].strategy}</span>
                    </div>
                </div>
            `
            wrapper.innerHTML += item
        }
    })
}

let expand = 1

let navbox = document.getElementsByClassName('dash-container')[0]
let viewbox = document.getElementsByClassName('views-container')[0]

let arrow = document.getElementsByClassName('arrow')[0]

let dashm = document.getElementsByClassName('dash-main')[0]
let logo = document.getElementsByClassName('tb-text')[0]

let dashbt = document.getElementsByClassName('nav-element')
let dashmain = document.getElementsByClassName('dash-element')

let text = document.getElementsByClassName('nav-text')
let img = document.getElementsByClassName('nav-image')

arrow.addEventListener('click', () => {
    if (expand == 0) {
        arrow.style.transform = "rotate(0deg)"
        logo.textContent = 'Pu'
        logo.style.border.left = "solid 1px #0EFB85"
        navbox.style.width = "5%"
        viewbox.style.width = "95%"
        for (let i = 0; i < text.length; i++) {
            text[i].style.display = 'none'
            img[i].style.display = 'block'
        }
        expand = 1
    } else {
        arrow.style.transform = "rotate(180deg)"
        logo.textContent = 'PlutoniumTrade'
        logo.style.border = "none"
        navbox.style.width = "15%"
        viewbox.style.width = "85%"
        for (let i = 0; i < text.length; i++) {
            text[i].style.display = 'block'
            img[i].style.display = 'none'
        }
        expand = 0
    }
})

logo.addEventListener('click', () => {
    dashm.style.display = 'block'
    for (let i = 0; i < dashmain.length; i++) {
        dashmain[i].style.display = 'none'
    }
})

for (let i = 0; i < dashbt.length; i++) {
    dashbt[i].addEventListener('click', () => {
        dashm.style.display = 'none'
        for (let e = 0; e < dashbt.length; e++) {
            if (e == i) {
                dashmain[e].style.display = 'block'
            } else {
                dashmain[e].style.display = 'none'
            }
        }
    })
}