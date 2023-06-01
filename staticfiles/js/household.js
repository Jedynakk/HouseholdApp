const expensesButton = document.getElementById('expensesButton')
const shoppingListButton = document.getElementById('shoppingListButton')
const toDoButton = document.getElementById('toDoButton')
const expensesModule = document.getElementById('expenses')
const shopingListModule = document.getElementById('shopingList')
const toDoModule = document.getElementById('toDo')



expensesButton.addEventListener("click", ShowExpenses)
shoppingListButton.addEventListener("click", ShowShoppingList)
toDoButton.addEventListener("click", ShowToDoList)



function ShowExpenses() {
    if (expensesModule.className == "hidden")
        expensesModule.className = "expenses";

    else
        expensesModule.className = "hidden"
    shopingListModule.className = "hidden",
        toDoModule.className = "hidden";
}


function ShowShoppingList() {
    if (shopingListModule.className == "hidden")
        shopingListModule.className = "shoppinglist";

    else
        shopingListModule.className = "hidden"
    expensesModule.className = "hidden",
        toDoModule.className = "hidden";
}



function ShowToDoList() {
    if (toDoModule.className == "hidden")
        toDoModule.className = "todo";

    else
        toDoModule.className = "hidden"
    expensesModule.className = "hidden",
        shopingListModule.className = "hidden"
}