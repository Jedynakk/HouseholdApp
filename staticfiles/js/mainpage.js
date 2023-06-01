

const createHouseholdForm = document.getElementById('createHouseholdForm')
const joinHouseholdForm = document.getElementById('joinHouseholdForm')

const createHouseholdButton = document.getElementById('createHousehold')
const joinHouseholdButton = document.getElementById('joinHousehold')



createHouseholdButton.addEventListener("click", DispalyCreateForm)
joinHouseholdButton.addEventListener("click", DispalyJoinForm)

function DispalyJoinForm() {
    if (joinHouseholdForm.className == 'hidden')
        joinHouseholdForm.className = 'displayedForm',
            createHouseholdForm.className = 'hidden';
    else
        joinHouseholdForm.className = 'hidden'
}



function DispalyCreateForm() {
    if (createHouseholdForm.className == 'hidden')
        createHouseholdForm.className = 'displayedForm',
            joinHouseholdForm.className = 'hidden';
    else
        createHouseholdForm.className = 'hidden'
}

