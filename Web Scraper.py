html>
    <head></head>
    <body>
        <script>
            let x=prompt("Enter a number:");
            let sum=0;
            while(x>0)
            {
                sum+=x%10;
                x=Math.floor(x/10);
            }
            alert("sum of individualdigits is:"+sum);
        </script>
    </body>
</html>
