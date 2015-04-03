# Lesson 2 Notes

## Forms

```
<form>

</form>
```

## Inputs

```
<input>
```

### Text box

``` 
<input name="q"> 
```

Whatever is typed in box will be updated in url after enter is pressed

### Button

``` 
<input type="submit"> 
```

## Form Attributes

### Action

```
<form action="http://www.google.com/search">
    <input name="q">
    <input type="submit">
</form>
```

Changes where a form submits too; above submits to google's search

### Methods - GET (default) , POST

```
<form method="post" action="/testform">
    <input name="q">
    <input type="submit">
</form>
```

GET - gets parameters from the url

```
http://localhost:8080/testform?q=hello+world
```

POST - puts the parameters in the body of the request; in the request text there will be the text q=hello+world 

```
POST /testform HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.8
Cache-Control: max-age=0
Content-Length: 13
Content-Type: application/x-www-form-urlencoded; charset="utf-8"
Content_Length: 13
Content_Type: application/x-www-form-urlencoded
Host: localhost:8080
Origin: http://localhost:8080
Referer: http://localhost:8080/
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36
X-Appengine-Country: ZZ

q=hello+world
```

## GET vs. POST

### GET parameters from requests - links in pages are GET requests

- parameters in url
- used for fetching documents; which document we are looking for; what page are we on
- affected by maximum url length; you can only encode so many paramters; ~2000 characters
- ok to cache
- should not change the server

### POST parameters from requests

- parameter in body (of request)
- used for updating data; make changes to data on server
- no maximum length; maybe on size 200MB?
- not ok to cache 
- ok to change the server
