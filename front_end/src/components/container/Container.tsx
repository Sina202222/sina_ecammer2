import React  from 'react'

interface Container{
    children: React.ReactNode;
  }

  function Container({ children }: Container) {

   const wlr ={
      maxWidth: '90%', /* container به طور پیش فرض عرض حداکثر 100% است و به صورت واکنش‌گرا تنظیم می‌شود */
      marginLeft: 'auto', /* mx-auto */
      marginRight: 'auto', /* mx-auto */
    }


    return (
      <div 
        className="container mx-auto " 
        style={wlr}
      >
        {children}
      </div>
    );
  }

export default Container