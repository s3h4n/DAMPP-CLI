<!doctype html>
<html lang='en'>

<head>
    <title>DAMP</title>
    <!-- Required meta tags -->
    <meta charset='utf-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1, shrink-to-fit=no'>

    <style>
        body {
            font-family: Ubuntu, sans-serif;
        }

        div {
            padding: 0.5rem;
        }

        a {
            text-decoration: none;
        }

        .center {
            background-color: white;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
            transition: 0.3s;
            border-radius: 12.5px;
            padding: 2rem;
            margin: 0;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
        }

        .center:hover {
            box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
        }

        .btn {
            padding: 10px 35.5px 10px 35.5px;
            margin-top: 15px;
            color: white;
            background-color: crimson;
            border: 0px;
            border-radius: 30px;
            font-size: 2.4vh;
            font-weight: bold;
        }

        .btn:hover {
            background-color: black;
            color: white;
            font-weight: bold;
        }

        .tracking-in-contract {
            -webkit-animation: tracking-in-contract 0.8s cubic-bezier(0.215, 0.610, 0.355, 1.000) both;
            animation: tracking-in-contract 0.8s cubic-bezier(0.215, 0.610, 0.355, 1.000) both;
        }

        @-webkit-keyframes tracking-in-contract {
            0% {
                letter-spacing: 1em;
                opacity: 0;
            }

            40% {
                opacity: 0.6;
            }

            100% {
                letter-spacing: normal;
                opacity: 1;
            }
        }

        @keyframes tracking-in-contract {
            0% {
                letter-spacing: 1em;
                opacity: 0;
            }

            40% {
                opacity: 0.6;
            }

            100% {
                letter-spacing: normal;
                opacity: 1;
            }
        }
    </style>

</head>

<body>

    <div class='center'>
        <span class='tracking-in-contract'>
            <a href='https://github.com/s3h4n/dampp.git'>
                <h1 style='color:crimson;'>DAMP</h1>
            </a>
            <h3>Dockerized Apache MySQL PHP</h3>
        </span>

        <hr />

        <div>
            <p>Customize <code style='color:deeppink; font-weight:bold;'>damp/index.php</code> to see the
                changes.</p>
        </div>

        <hr />

        <div>
            <button class='btn' type='button' onclick=' open_php_my_admin()'>
                PhpMyAdmin
            </button>
        </div>
    </div>

    <script defer>
        const open_php_my_admin = () => {
            window.open('http://localhost:8080/', '_blank');;
        };
    </script>

</body>

</html>