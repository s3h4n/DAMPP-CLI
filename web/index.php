<?php

$request = $_SERVER['REQUEST_URI'];

# Simple Router

switch ($request) {
	case '/':
		require __DIR__ . '/src/Index.php';
		break;
	case '':
		require __DIR__ . '/src/Index.php';
		break;
	default:
		break;
}

?>