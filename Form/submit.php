<?php
require 'C:\xampp\htdocs\Form\PHPMailer\src\Exception.php';
require 'C:\xampp\htdocs\Form\PHPMailer\src\PHPMailer.php';
require 'C:\xampp\htdocs\Form\PHPMailer\src\SMTP.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "test_db";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get form data
$user = $_POST['username'];
$email = $_POST['email'];
$phone = $_POST['phone'];
$pass = $_POST['password'];

// Insert data into table
$sql = "INSERT INTO users (username, email, phone, password) VALUES ('$user', '$email', '$phone', '$pass')";

if ($conn->query($sql) === TRUE) {
    // Send thank you email
    $mail = new PHPMailer(true);
    try {
        $mail->isSMTP();
        $mail->Host = 'smtp.gmail.com';
        $mail->SMTPAuth = true;
        $mail->Username = 'tempmailgeneral@gmail.com'; // Updated email
        $mail->Password = 'Abishek27'; // Use your actual password
        $mail->SMTPSecure = 'tls';
        $mail->Port = 587;

        $mail->setFrom('tempmailgeneral@gmail.com', 'Your Name'); // Updated email
        $mail->addAddress($email);
        $mail->addReplyTo('tempmailgeneral@gmail.com'); // Updated email
        $mail->Subject = 'Thank You for Your Submission';
        $mail->Body    = 'Thank you, '.$user.', for submitting your details!';

        $mail->send();
        echo "Thank you! Your details have been saved and an email has been sent to you.";
    } catch (Exception $e) {
        echo "Email sending failed: " . $mail->ErrorInfo;
    }
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
