import {create_alert, fade_out_element} from "./functions.js";

window.onload = async () => {
    let user_form = document.querySelector('#user-form');
    user_form.addEventListener('submit', async function(e) {
        e.preventDefault()
        let token = this.querySelector('input[name="token"]');
        let user_id = this.querySelector('input[name="user_id"]');
        let first_name = this.querySelector('input[name="first_name"]');
        let last_name = this.querySelector('input[name="last_name"]');
        let email = this.querySelector('input[name="email"]');
        let username = this.querySelector('input[name="username"]');
        let phone = this.querySelector('input[name="phone"]');
        let date_of_birth = this.querySelector('input[name="date_of_birth"]');

        let form_data = new FormData();
        form_data.append('token', token.value);
        form_data.append('user_id', user_id.value);
        form_data.append('first_name', first_name.value);
        form_data.append('last_name', last_name.value);
        form_data.append('email', email.value);
        form_data.append('username', username.value);
        form_data.append('phone', phone.value);
        form_data.append('date_of_birth', date_of_birth.value);
        let result = await fetch("http://localhost:5000/api/update/user", {
            method: "POST",
            body: form_data
        });

        let data = await result.json();
        console.log(data);
        if (data.status == 200) {
            let user = data.user;
            first_name.value = user.FirstName;
            last_name.value = user.LastName;
            email.value = user.Email;
            username.value = user.Username;
            phone.value = user.PhoneNumber;
            date_of_birth.value = user.DateOfBirth;
            let header = document.querySelector('.container > .header');
            header.innerText = `Profile for ${user.Username}`;
            let alert = create_alert(data.category, data.message);
            fade_out_element(alert);

        } else {
            let alert = create_alert(data.category, data.message);
            fade_out_element(alert);
        }

    });
}