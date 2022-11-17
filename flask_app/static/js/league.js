
var submit = document.querySelector('#submit')
let teams = document.querySelectorAll('.team-table')
var all_tables = document.querySelector('#all_teams')
var all_players = document.querySelectorAll(".player-row")
let toggle = document.querySelector('#checked-toggle')
let assetDisplay = document.querySelector('#display_assets')

teams.forEach(team => {
    topAssets(team.getAttribute('team'))
})


toggle.addEventListener('click', () =>{
    if(toggle.checked === true){
        assetDisplay.innerHTML = "Displaying Top Five Assets"
    teams.forEach(team => {
        topAssets(team.getAttribute('team'))

    })
} else {
    allAssets()
    assetDisplay.innerHTML = "Displaying All Assets"
}
})


function topAssets(teamName) {
    console.log(teamName)
    let id = teamName
    let appendTarget = document.getElementById(id)
    let values = []
    let valuesObj = {}
    let topTenValues = []

    let players = document.querySelectorAll(`.${teamName}`)
    players.forEach(player => {
        let value = parseInt(player.getAttribute('player-value'))
        if (values.includes(value) === false) {
            values.push(value)
        }
        if (valuesObj[value]) {
            valuesObj[value].push(player)
        } else {
            valuesObj[value] = [player]
        }
    })

    values.shift()
    topTenValues = values.sort((a, b) => b - a).slice(0,5)
    let count = 0
    console.log(values)
    console.log(topTenValues)
    topObj = {}
    
    for(var i = 0; i < topTenValues.length; i++){
        topObj[topTenValues[i]] = valuesObj[topTenValues[i]]
    }

    players.forEach(player => {
        if (Object.keys(topObj).indexOf(player.getAttribute('player-value')) === -1 || count >= 5) {
            player.classList.add('hidden')
        } else {
            count++
        }
    })

    
}


function allAssets() {
    all_players.forEach(player => { 
        // console.log(player)
        player.classList.remove('hidden')
    })
}




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




