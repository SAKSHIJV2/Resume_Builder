<?php
include 'database.php'; // Ensure this file exists

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $fullname = $_POST['fullname'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $password = password_hash($_POST['password'], PASSWORD_DEFAULT);

    $sql = "INSERT INTO user (fullName, email, phoneNumber, password) VALUES ('$fullname', '$email', '$phone', '$password')";

    if ($conn->query($sql) === TRUE) {
        // Redirect to thirdpage.html
        header("Location: ../frontend/thirdpage.html");
        exit(); // Always call exit after header redirect
    } else {
        echo "❌ Error: " . $conn->error;
    }
}
?>
