
today = document.getElementById("today")

date =  new Date()
const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
correct_month = months[date.getMonth()]
const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
new_day = days[date.getDay()]
curent_date = new_day+' '+date.getDate()+' '+correct_month+' '+date.getFullYear()
today.innerHTML = curent_date
