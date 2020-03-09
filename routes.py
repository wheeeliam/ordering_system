from flask import render_template, request, url_for, redirect
from server import app, system
from forms import OrderStatusForm
from inventory import Inventory, ItemError

'''
Dedicated page for "page not found"
'''
@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404

'''
Homepage
'''
@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if "create_order" in request.form:
            # create order and go to order.html
            order = system.create_order_in_orders()
            return redirect(url_for('order', order_id=order))
            
    return render_template("home.html")


@app.route('/order/<order_id>', methods=["GET", "POST"])
def order(order_id):
    # TODO - print this out to website
    order = system.get_order_str(order_id)
    system.orders[system.get_index_of_order_id(order_id)].compute_total_price()

    if request.method == "POST":
        # just rendering templates for now
        if 'add_main' in request.form:
            return redirect(url_for('main', order_id=order_id))
        elif 'add_side' in request.form:
            return redirect(url_for('side', order_id=order_id))
        elif 'checkout' in request.form:
            return redirect(url_for('checkout', order_id=order_id))
    
    return render_template("order.html", order=order)

'''
Route for main order selection
'''
from main import *
@app.route('/order/<order_id>/main', methods=["GET", "POST"])
def main(order_id):
    # generate base menu and ingredients list from inventory
    menu_list = system.inventory.base_menu_gen()
    ingrs = system.inventory.ingr_gen('main')
    for ingr in ingrs:
        if 'wrap' in ingr:
            ingrs.remove(ingr)      # making default list of ingredients without wraps for burgers
                                    # - regenerated later without buns for wraps
    
    if request.method == "POST":
        selected_menu_item = request.form.get('menu_item')      # retreive user selected base item
        l = selected_menu_item.split(", ")                      # parse user selected base item
            
        if 'check' in request.form or 'confirm' in request.form:
            selected_custom = request.form.get('custom')
            custom_all = []         # custom list for all ingredients
            custom_bwp = []         # custom list for buns, wraps and patties
            custom_ingr = {}        # custom list for all other ingredients

            for x in range(10):
                custom_all.append(request.form.get(str(x)))

            if selected_custom == 'yes':
                for item in custom_all:
                    if 'bun' in item or 'wrap' in item or 'patty' in item:
                        custom_bwp.append(item)
                    else:
                        if item in custom_ingr:
                            custom_ingr[item] += 1
                        else:
                            custom_ingr[item] = 1
                del custom_ingr["None"]
            
            # dictionary that will be used to create order
            d = {}
            bun_type = None
            patty_type = None
            wrap_type = None

            # instantiate the base objects if selected
            if 'Single' in l[0]:
                if selected_custom == 'no':
                    d = {l[1]: 2, l[2]:1}
                elif selected_custom == 'yes':
                    for item in custom_bwp:
                        if 'bun' in item:
                            bun_type = item
                        if 'patty' in item:
                            patty_type = item

                    if bun_type is None:
                        bun_type = l[1]                    
                    if patty_type is None:
                        patty_type = l[2]
                    d = {bun_type: 2, patty_type: 1}

                    d.update(custom_ingr)
                    print(d)
                item = Single_Burger(d, system.inventory)
            
            if 'Double' in l[0]:
                if selected_custom == 'no':
                    d = {l[1]: 3, l[2]:2}
                elif selected_custom == 'yes':
                    for item in custom_bwp:
                        if 'bun' in item:
                            bun_type = item
                        if 'patty' in item:
                            patty_type = item

                    if bun_type is None:
                        bun_type = l[1]                    
                    if patty_type is None:
                        patty_type = l[2]
                    d = {bun_type: 3, patty_type: 2}

                    d.update(custom_ingr)
                    print(d)
                item = Double_Burger(d, system.inventory)
            
            if 'Triple' in l[0]:
                if selected_custom == 'no':
                    d = {l[1]: 4, l[2]:3}
                elif selected_custom == 'yes':
                    for item in custom_bwp:
                        if 'bun' in item:
                            bun_type = item
                        if 'patty' in item:
                            patty_type = item

                    if bun_type is None:
                        bun_type = l[1]                    
                    if patty_type is None:
                        patty_type = l[2]
                    d = {bun_type: 4, patty_type: 3}

                    d.update(custom_ingr)
                    print(d)
                item = Triple_Burger(d, system.inventory)
            
            if 'Wrap' in l[0]:
                d[l[1]] = 1
                d[l[2]] = 1
                if selected_custom == 'no':
                    d = {l[1]: 1, l[2]:1}
                elif selected_custom == 'yes':
                    for item in custom_bwp:
                        if 'wrap' in item:
                            wrap_type = item
                        if 'patty' in item:
                            patty_type = item

                    if wrap_type is None:
                        wrap_type = l[1]                    
                    if patty_type is None:
                        patty_type = l[2]
                    d = {wrap_type: 1, patty_type: 1}

                    d.update(custom_ingr)
                    print(d)
                item = Wrap(d, system.inventory)

                # re-generate the ingrs to remove buns instead of wraps
                ingrs = system.inventory.ingr_gen('main')
                for ingr in ingrs:
                    if 'bun' in ingr:
                        ingrs.remove(ingr)
            
            # if user confirms, add to order
            if 'confirm' in request.form:
                system.add_item_to_order(item, order_id)
                return redirect(url_for('order', order_id=order_id))
            else:
                # display price before redirect
                price = item.item_price
                return render_template("main.html", menu_list=menu_list, selected_menu_item=selected_menu_item, selected_custom=selected_custom, price=price, ingrs=ingrs, custom_all=custom_all)


        if 'select' in request.form:
            selected_custom = request.form.get('custom')
            # re-render with custom
            if selected_custom == 'yes':
                if 'Wrap' in l[0]:
                    ingrs = system.inventory.ingr_gen('main')
                    print (ingrs)
                    for ingr in ingrs:
                        print (ingr)
                        if 'bun' in ingr:
                            ingrs.remove(ingr)
                return render_template("main.html", menu_list=menu_list, selected_menu_item=selected_menu_item, selected_custom=selected_custom, ingrs=ingrs)
            else:
                return render_template("main.html", menu_list=menu_list, selected_menu_item=selected_menu_item, selected_custom=selected_custom)
    
    return render_template("main.html", menu_list=menu_list)


'''
Route for side selection
'''
from side import *
@app.route('/order/<order_id>/side', methods=["GET", "POST"])
def side(order_id):
    sides = ['6 Pack Nuggets', '3 Pack Nuggets', 'Medium Fries', 'Small Fries']
    sides += system.inventory.ingr_gen('side')
    sides.remove('fries')
    sides.remove('nuggets')

    if request.method == "POST":
        selected_side_item = request.form.get('side_item')
        print (selected_side_item)

        if "check" in request.form or 'confirm' in request.form:

            # if side selected is a drink
            if "ml" in selected_side_item:
                item = Drink(selected_side_item, 1, system.inventory)
            
            if  selected_side_item == "6 Pack Nuggets":
                item = Nuggets(selected_side_item, 1, system.inventory)
                print (item.item_price)
                
            
            if  selected_side_item == "3 Pack Nuggets":
                item = Nuggets(selected_side_item, 1, system.inventory)
            
            if  selected_side_item == "Medium Fries":
                item = Fries(selected_side_item, 1, system.inventory)
            
            if  selected_side_item == "Small Fries":
                item = Fries(selected_side_item, 1, system.inventory)
 
            if 'confirm' in request.form:
                system.add_item_to_order(item, order_id)
                return redirect(url_for('order', order_id=order_id))
            else:
                price = item.item_price
                return render_template("side.html", sides=sides, selected_side_item=selected_side_item, price=price)

    return render_template("side.html", sides=sides)


'''
Route for order confirmation
'''
@app.route('/order/<order_id>/order_confirmation/', methods=["GET", "POST"])
def checkout(order_id):
   
    system.update_order_status('Kitchen Received', order_id)
    system.update_inventory_order(order_id)
    system.view_order(order_id)

    status = system.get_order_status(order_id)
    price = system.orders[system.get_index_of_order_id(order_id)].total_price

    return render_template("order_confirmation.html",order_id=order_id, status=status, price=price)

'''
Function to fetch status of an order
'''
@app.route('/order_status', methods=["GET","POST"])
def order_status():
    if 'order_id' in request.form:
        form = OrderStatusForm(request.form.get("order_id"))

        if form.is_valid is not True:
            return render_template("order_status.html", form=form)
        
        # actually print out the order status
        status = system.get_order_status(form.order_id)
        return render_template("order_status.html", status=status)

    return render_template("order_status.html")

'''
Admin homepage
'''
@app.route('/admin')
def admin():
    return render_template("admin.html")

@app.route('/update_inventory', methods=["GET","POST"])
def update_inventory():
    errors = []
    inventory = {}

    for index, i in enumerate(system.inventory._dict.items()):
        item = list(system.inventory._dict.keys())[index]
        qty = system.inventory._dict[i[0]].qty_remaining
        inventory[item] = qty

    if request.method == "POST":
        if request.form['action'] == 'update':
            try:
                print('TRY')
                system.inventory.update_item_quantity(request.form['item'], int(request.form['qty']))
                inventory[request.form['item']] = int(request.form['qty'])

            except ItemError as err:
                print('ERR', err)
                errors.append(str(err))

    print('ERRORS', errors)

    return render_template("update_inventory.html", 
                            inventory=inventory, 
                            errors=errors)

@app.route('/order_list', methods=["GET", "POST"])
def order_list():
    orders = system.orders

    if request.method == "POST":
        if request.form['action'] == 'delete':
            order_id_index = system.get_index_of_order_id(request.form['id'])
            system.remove_order_by_id(order_id_index)
        if request.form['action'] == 'update':
            order_id = request.form['id']
            select = request.form.get('order_status')
            print('select', select)
            system.update_order_status(select, order_id)

    return render_template("order_list.html", 
                           orders=orders)
