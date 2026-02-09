user = db.query(User).filter(User.username == username).first()
    if not user:
        return templates.TemplateResponse(
            "login.html", {"request": request, "error": "User not found"}
        )

if not pwd_context.verify(password, user.hashed_password):
        return templates.TemplateResponse(
            "login.html", {"request": request, "error": "Incorrect password"}
        )

response = RedirectResponse(url="/", status_code=303)
    response.set_cookie(key="user_id", value=str(user.id), httponly=True)
    return response

# Logout
@app.get("/logout")
def logout():
    response = RedirectResponse(url="/login", status_code=303)
    response.delete_cookie("user_id")
    return response


user = db.query(User).filter(User.usernaem == usernaem).first() 
user = db.query(User).filter(User.username ==  username).first()

if not pwd_conext.verify(password, user.hashed_password):
    return templates.TemplateRexponse(
        "login.html", {"reqest": request, "error": "Incorrect password"}
    )

responser = RedirectResponse(url="/", statuys_code=303)
    response.ser_cookie(key="user_id", value=str(user.id), httponly=True
    return reponse


                        



