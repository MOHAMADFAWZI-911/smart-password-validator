from flask import Flask, render_template, request, session, redirect, url_for
import itertools
import math
import string

app = Flask(__name__)
app.secret_key = 'Security_Project_Super_Secret_Key_2025'

def calculate_strength(password):
    pool_size = 0
    if any(c.islower() for c in password): pool_size += 26
    if any(c.isupper() for c in password): pool_size += 26
    if any(c.isdigit() for c in password): pool_size += 10
    if any(c in string.punctuation for c in password): pool_size += 32
    
    length = len(password)
    # Multiplication Rule: N^L
    total_combinations = math.pow(pool_size, length) if pool_size > 0 else 0
    entropy = math.log2(total_combinations) if total_combinations > 0 else 0
    
    return length, pool_size, total_combinations, entropy

# Helper function to generate permutations on-the-fly
def generate_blacklist(user_data_dict):
    base_data = {
        user_data_dict.get('fname'), 
        user_data_dict.get('lname'), 
        user_data_dict.get('year'), 
        user_data_dict.get('partner'), 
        user_data_dict.get('pet'), 
        user_data_dict.get('mobile')
    }
    base_data = {w for w in base_data if w} 
    
    processed_data = set()
    for item in base_data:
        processed_data.add(item)
        processed_data.add(item.lower())
        processed_data.add(item.upper())
        processed_data.add(item.capitalize())
        
    weak_set = set()
    weak_set.update(processed_data)
    
    # Mathematical Permutations (nPr)
    # We limit to 2 and 3 combinations to keep performance high for the demo
    perms_2 = list(itertools.permutations(processed_data, 2))
    for p in perms_2: weak_set.add("".join(p))
    
    perms_3 = list(itertools.permutations(processed_data, 3))
    for p in perms_3: weak_set.add("".join(p))
    
    return weak_set

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    
    if request.method == 'POST' and 'reset_action' in request.form:
        session.clear()
        return redirect(url_for('index'))

    if request.method == 'POST' and 'save_data' in request.form:
        user_data = {
            'fname': request.form.get('fname', '').strip(),
            'lname': request.form.get('lname', '').strip(),
            'year': request.form.get('year', '').strip(),
            'partner': request.form.get('partner', '').strip(),
            'pet': request.form.get('pet', '').strip(),
            'mobile': request.form.get('mobile', '').strip()
        }
        
        session['user_data'] = user_data
        session['data_loaded'] = True
        session['user_name'] = user_data['fname'] if user_data['fname'] else "Target"
        
        temp_blacklist = generate_blacklist(user_data)
        session['blacklist_count'] = len(temp_blacklist)
        
        return redirect(url_for('index'))

    if request.method == 'POST' and 'check_pass' in request.form:
        target_password = request.form.get('password', '')
        
        if 'user_data' in session:
            current_blacklist = generate_blacklist(session['user_data'])
            is_weak = False
            weak_reason = ""

            # Set Membership Check
            if target_password in current_blacklist:
                is_weak = True
                weak_reason = "Direct match with personal data permutation!"
            else:
                for item in current_blacklist:
                    if item and len(item) > 3 and item in target_password:
                        is_weak = True
                        weak_reason = f"Contains personal sequence: '{item}'"
                        break
            
            if is_weak:
                result = {
                    "status": "danger",
                    "title": "Unsafe Password!",
                    "msg": weak_reason,
                    "note": "Mathematical Logic: Matches generated personal permutations set."
                }
            else:
                length, pool, combs, entropy = calculate_strength(target_password)
                strength_label = "Very Strong" if entropy > 60 else "Moderate" if entropy > 40 else "Weak"
                css_class = "success" if entropy > 60 else "warning" if entropy > 40 else "danger"
                
                result = {
                    "status": css_class,
                    "title": f"Password Accepted ({strength_label})",
                    "length": length,
                    "pool": pool,
                    "combs": f"{combs:.2e}",
                    "entropy": f"{entropy:.2f}"
                }

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)