window.onload = async () => {
    let user_form = document.querySelector('#user-form');
    user_form.addEventListener('submit', async function(e) {
        e.preventDefault();
        let user_id = this.querySelector('input[name="user_id"]').value;
        let first_name = this.querySelector('input[name="first_name"]').value;
        let last_name = this.querySelector('input[name="last_name"]').value;
        let email = this.querySelector('input[name="email"]').value;
        let username = this.querySelector('input[name="username"]').value;
        let phone = this.querySelector('input[name="phone"]').value;
        let date_of_birth = this.querySelector('input[name="date_of_birth"]').value;
        console.log(first_name);
        console.log(last_name);
        console.log(email);
        console.log(username);
        console.log(phone);
        console.log(date_of_birth);
        let form_data = new FormData();
        form_data.append('user_id', user_id);
        form_data.append('first_name', first_name);
        form_data.append('last_name', last_name);
        form_data.append('email', email);
        form_data.append('username', username);
        form_data.append('phone', phone);
        form_data.append('date_of_birth', date_of_birth);
        await fetch("http://localhost:5000/api/update/user", {
            method: "POST",
            body: form_data
        });
    });
}