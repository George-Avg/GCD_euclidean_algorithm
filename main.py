# Οδηγίες
print("Οδηγίες:"
      "\nΓια να υπολογιστεί ο Μ.Κ.Δ και το Ε.Κ.Π. πρέπει μετά την φράση "
      "\n<< Εισάγετε τους αριθμούς: >> να πληκτρολογηθούν οι ακέραιοι αριθμοί"
      "\nμε ένα κενό (space) μεταξύ τους και να πατηθεί το ENTER στο τέλος. \n\n")


# Συνάρτηση για μετατροπή string σε integer και απόλυτο
def fix_nums(num):
    num = abs(int(num))
    return num


# Εισαγωγή αριθμών στη λίστα/ έλεγχος εγκυρότητας
try:
    numbers_list = list(map(fix_nums, input("Εισάγετε τους αριθμούς: ").split()))
except:
    print("Βρέθηκε πρόβλημα. Σιγουρευτείτε ότι οι αριθμοί είναι ακέραιοι.")
    input("\nΠατήστε ENTER δυο φορές για να κλείσει η εφαρμογή")
    input()
    quit()


# Συνάρτηση για τον αλγόριθμο του Ευκλείδη
def euclidean_algorithm(dividend, divisor):
    while divisor != 0:
        remainder = dividend % divisor
        quotient = dividend // divisor

        print(f"⇔ {dividend} = {quotient} * {divisor} + {remainder}")

        dividend = divisor
        divisor = remainder

    return dividend


# Εύρεση Μ.Κ.Δ. μέσο του αλγόριθμου του Ευκλείδη
print("\n\n\nΥπολογισμός Μ.Κ.Δ χρησιμοποιώντας τον Αλγόριθμο του Ευκλείδη:")
gcd = 0  # Ουδέτερος αριθμός για το πρώτο Μ.Κ.Δ.
for list_item in numbers_list:
    print("\nΝέος Μ.Κ.Δ:"
          "\nΔιαιρετέος = πηλίκο * διαιρέτης + υπόλοιπο")
    gcd = euclidean_algorithm(gcd, list_item)

# Εύρεση Ε.Κ.Π. μέσο της σχέσης: lcm = product / gcd:
product = 1  # Ουδέτερος αριθμός για το πρώτο γινόμενο
for list_item_2 in numbers_list:
    product = product * list_item_2
lcm = int(product / gcd)

# Αποτελέσματα
print("\n\n\n↑ ↑ ↑  Διαδικασία εύρεσης Μ.Κ.Δ.  ↑ ↑ ↑")
print("\nΑποτελέσματα:")
print(f"\nΑριθμοί: {numbers_list}"
      f"\nΜ.Κ.Δ.: {gcd}"
      f"\nΕ.Κ.Π.: {lcm}")

input("\nΠατήστε ENTER δυο φορές για να κλείσει η εφαρμογή")
input()
123