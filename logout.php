<?php
session_start();
session_destroy(); // Destroy the session
header("Location: ../frontend/index.html"); // Redirect to the main page
exit();
?>
