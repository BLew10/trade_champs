
const teamASum = document.querySelector('#A_total')
const teamBSum = document.querySelector('#B_total')
const draggables = document.querySelectorAll('.draggable');
const teams = document.querySelectorAll('.team');
const qbs = document.querySelectorAll('.QB')
const rbs = document.querySelectorAll('.RB')
const wrs = document.querySelectorAll('.WR')
const tes = document.querySelectorAll('.TE')
const players = document.querySelectorAll('.player')
const searchAll = document.querySelector('#search_all')
const searchQb = document.querySelector('#search_qb')
const searchRb = document.querySelector('#search_rb')
const searchWr = document.querySelector('#search_wr')
const searchTe = document.querySelector('#search_te')
const placeholderA = document.querySelector('#team_a')
const placeholderB = document.querySelector('#team_b')
const a = document.querySelector('#A')
const b = document.querySelector('#B')
const aTeam = document.querySelectorAll(".a-team")
const bTeam = document.querySelectorAll(".b-team")
let isNotEmptyA = false
let isNotEmptyB = false
let sumA = 0
let sumB = 0
let count = 0

searchAll.addEventListener('input', () => {
    let name = searchAll.value.toLowerCase()
    const all_display = document.querySelector('#all_display')
    all_display.innerHTML = '';
    for (var i = 0; i < players.length; i++) {
        player_name = players[i].getAttribute('name')
        player_name = player_name.toLowerCase()
        if (player_name.includes(name)  && !players[i].classList.contains('a-team') && !players[i].classList.contains('b-team')) {
            all_display.appendChild(players[i])
        }

    }
}
)


searchQb.addEventListener('input', () => {
    let name = searchQb.value.toLowerCase()
    const qb_display = document.querySelector('#qb_display')
    qb_display.innerHTML = '';
    for (var i = 0; i < qbs.length; i++) {
        player_name = qbs[i].getAttribute('name')
        player_name = player_name.toLowerCase()
        if (player_name.includes(name)  && !qbs[i].classList.contains('a-team') && !qbs[i].classList.contains('b-team')) {
            qb_display.appendChild(qbs[i])
        }

    }
}
)


searchRb.addEventListener('input', () => {
    let name = searchRb.value.toLowerCase()
    const rb_display = document.querySelector('#rb_display')
    console.log(rb_display)
    rb_display.innerHTML = '';
    for (var i = 0; i < rbs.length; i++) {
        player_name = rbs[i].getAttribute('name')
        player_name = player_name.toLowerCase()
        if (player_name.includes(name) && !rbs[i].classList.contains('a-team') && !rbs[i].classList.contains('b-team')) {

            rb_display.appendChild(rbs[i])
        
        }

    }
}
)
searchTe.addEventListener('input', () => {
    let name = searchTe.value.toLowerCase()
    const te_display = document.querySelector('#te_display')
    te_display.innerHTML = '';
    for (var i = 0; i < tes.length; i++) {
        player_name = tes[i].getAttribute('name')
        player_name = player_name.toLowerCase()
        if (player_name.includes(name) && !tes[i].classList.contains('a-team') && !tes[i].classList.contains('b-team')) {
            te_display.appendChild(tes[i])
        }

    }
}
)
searchWr.addEventListener('input', () => {
    let name = searchWr.value.toLowerCase()
    const wr_display = document.querySelector('#wr_display')
    wr_display.innerHTML = '';
    for (var i = 0; i < wrs.length; i++) {
        player_name = wrs[i].getAttribute('name')
        player_name = player_name.toLowerCase()
        console.log(wrs[i].classList.contains('a-team'), "*********")
        if (player_name.includes(name)  && !wrs[i].classList.contains('a-team') && !wrs[i].classList.contains('b-team')) {
            wr_display.appendChild(wrs[i])
        }

    }
}
)




draggables.forEach(player => {

    attachedDraggableEvent(player)
    // player.addEventListener('dragstart', () => {
    //     player.classList.add('dragging')
    // });
    // player.addEventListener('dragend', () => {
    //     player.classList.remove('dragging')
    // });
})

function attachedDraggableEvent(el) {
    el.addEventListener('dragstart', () => {
        el.classList.add('dragging')
    });
    el.addEventListener('dragend', () => {
        el.classList.remove('dragging')
    });
}
/* drop targets */

teams.forEach(team => {
    team.addEventListener('dragover', (e) => {

        if (isNotEmptyA === false && team.getAttribute('id') === "team_a") {
            placeholderA.innerHTML = ''
            isNotEmptyA = true
        } else if (isNotEmptyB === false && team.getAttribute('id') === "team_b") {
            placeholderB.innerHTML = ''
            isNotEmptyB = true
        }
        e.preventDefault()
        const draggable = document.querySelector('.dragging')
        team.appendChild(draggable)
        
        if (team.getAttribute('id') === "team_a") {
            draggable.classList.add('a-team')
            draggable.classList.remove('b-team')
        } else if (team.getAttribute('id') === "team_b") {
            draggable.classList.add('b-team')
            draggable.classList.remove('a-team')
        } else {
            draggable.classList.remove('a-team')
            draggable.classList.remove('b-team')
        }
        addTotal()





    })
})

function addTotal() {
    sumA = 0
    sumB = 0
    const aTeam = document.querySelectorAll(".a-team")
    const bTeam = document.querySelectorAll(".b-team")
    aTeam.forEach(player => {
        sumA += parseInt(player.getAttribute('value'))
    })

    bTeam.forEach(player => {
        sumB += parseInt(player.getAttribute('value'))
    })
    document.querySelector('#A_total').innerText = `Value: ${sumA}`
    document.querySelector('#B_total').innerText = `Value: ${sumB}`

    if (sumA > sumB) {
        document.getElementById("A_total").style.color = "#22c55e";
        document.getElementById("B_total").style.color = "#ef4444";
    } else if (sumB > sumA) {
        document.getElementById("A_total").style.color = "#ef4444";
        document.getElementById("B_total").style.color = "#22c55e";
    } else {
        document.getElementById("A_total").style.color = "#94a3b8";
        document.getElementById("B_total").style.color = "#94a3b8";
    }

    let fair = acceptedVariance(sumA, sumB)

    if (sumA > sumB && fair === false) {
        document.querySelector('#winner').innerHTML = 'A Wins Trade'
        document.querySelector('#winner').classList.remove('text-purple-700')

    } else if (sumB > sumA && fair === false) {
        document.querySelector('#winner').innerHTML = 'B Wins Trade'
        document.querySelector('#winner').classList.remove('text-purple-700')
    } else if (sumB === 0 && sumA === 0) {
        document.querySelector('#winner').innerHTML = ''
    } else {
        document.querySelector('#winner').innerHTML = 'Fair Trade'
        document.querySelector('#winner').classList.add('text-purple-700')
    }
}




teams.forEach(team => {
    const draggable = document.querySelector('.dragging')
    team.addEventListener('dragleave', (e) => {
        if (placeholderA.innerHTML === '') {
            placeholderA.appendChild(a)
            isNotEmptyA = false
        }
        if (placeholderB.innerHTML === '') {
            placeholderB.appendChild(b)
            isNotEmptyB = false
        }

        addTotal()
    })
})


teams.forEach(team => {
    team.addEventListener('drop', () => {
        const draggable = document.querySelector('.dragging')
        addTotal()
    })
})

let variance = document.querySelector('#variance')

function acceptedVariance(sumA, sumB) {
    let variance = document.querySelector('#variance')
    let accepetedVariance = parseInt(variance.value)
    let difference = (Math.abs(sumA - sumB)) / ((sumA + sumB) / 2) * 100
    console.log(accepetedVariance, difference)

    if (difference <= accepetedVariance) {
        console.log('true')
        return true
    } else {
        console.log('false')
        return false
    }
}

variance.addEventListener('change', () => {
    addTotal()
})

const menu = document.querySelector('#menu')
let menuIsOpen = false
menu.addEventListener('click', ()=> {
    console.log("working")
    if(!menuIsOpen) {
        document.querySelector('#navbar-default').classList.remove('hidden')
        menuIsOpen = true}
        else {
            document.querySelector('#navbar-default').classList.add('hidden')
        menuIsOpen = false
        }
})

