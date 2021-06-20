const inimigos = document.getElementsByClassName('inimigo')
const armas = document.getElementsByClassName('arma')
const btn = document.getElementById("dano")
dano_arma = 0
vida_inimigo = 0

for(const inimigo of inimigos){
    const nomeInimigo = inimigo.getAttribute('data-nome')
    const vidaInimigo = inimigo.getAttribute('data-vida')

    inimigo.addEventListener('click', function(){
        if(document.getElementsByClassName('inimigo-selecionado').length == 0){
            inimigo.classList.add('inimigo-selecionado')
            vida_inimigo = vidaInimigo
            alert(`${nomeInimigo} selecionado `)
        }else{
            inimigo.classList.remove('inimigo-selecionado')
        }
    })
}


for(const arma of armas){
    const nomeArma = arma.getAttribute('data-nome')
    const danoArma = arma.getAttribute('data-dano')

    arma.addEventListener('click', function(){
        if(document.getElementsByClassName('arma-selecionada').length == 0){
            arma.classList.add('arma-selecionada')
            dano_arma = danoArma
            alert(`${nomeArma}: ${danoArma}`)
        }else{
            arma.classList.remove('arma-selecionada')
        }
    })
}

function calcularDano(){
    if(dano_arma > vida_inimigo){
    btn.innerHTML =`Dano: ${dano_arma}! Você matou o inimigo!`
    
    }else{
    btn.innerHTML=`Dano: ${dano_arma}! O inimigo sobreviveu...`
    }
}