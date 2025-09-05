document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById("sendOtpBtn");

    btn.addEventListener("click", function () {
        let name = document.getElementById("name").value.trim();
        let phone = document.getElementById("phone").value.trim();
        let email = document.getElementById("email").value.trim();
        let city = document.getElementById("city").value;
        let pincode = document.getElementById("pincode").value.trim();

        // Clear previous errors
        document.getElementById("error-name").innerText = "";
        document.getElementById("error-phone").innerText = "";
        document.getElementById("error-email").innerText = "";
        document.getElementById("error-city").innerText = "";
        document.getElementById("error-pincode").innerText = "";

        let valid = true;

        if (!name) { document.getElementById("error-name").innerText = "Please enter your name."; valid=false; }
        let phonePattern = /^[6-9]\d{9}$/;
        if (!phone) { document.getElementById("error-phone").innerText = "Please enter your phone number."; valid=false; }
        else if (!phonePattern.test(phone)) { document.getElementById("error-phone").innerText = "Enter a valid 10-digit phone number."; valid=false; }

        let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!email) { document.getElementById("error-email").innerText = "Please enter your email."; valid=false; }
        else if (!emailPattern.test(email)) { document.getElementById("error-email").innerText = "Enter a valid email address."; valid=false; }

        if (!city) { document.getElementById("error-city").innerText = "Please select a city."; valid=false; }

        let pinPattern = /^\d{6}$/;
        if (!pincode) { document.getElementById("error-pincode").innerText = "Please enter pin code."; valid=false; }
        else if (!pinPattern.test(pincode)) { document.getElementById("error-pincode").innerText = "Enter a valid 6-digit pin code."; valid=false; }

        if (!valid) return;

        // OTP sent successfully
        alert("✅ OTP has been sent successfully!");

        // Clear fields
        document.getElementById("name").value = "";
        document.getElementById("phone").value = "";
        document.getElementById("email").value = "";
        document.getElementById("city").value = "";
        document.getElementById("pincode").value = "";
    });
});
