# Rosen Example 6: "The sum of two positive integers is always positive"

def implies(p, q):
    """p -> q  is the same as  (not p) or q"""
    return (not p) or q


# ---------- Version 1: domain = ALL integers ----------
# Logic:  ∀x ∀y ((x > 0) ∧ (y > 0) → (x + y > 0))
# We can't loop over infinitely many integers, so we test a sample.
integers = range(-10, 11)

version1 = all(
    implies(x > 0 and y > 0, x + y > 0)
    for x in integers
    for y in integers
)

# ---------- Version 2: domain = POSITIVE integers ----------
# Logic:  ∀x ∀y (x + y > 0)
positives = range(1, 11)

version2 = all(
    x + y > 0
    for x in positives
    for y in positives
)

print("Version 1 (domain = integers):         ", version1)
print("Version 2 (domain = positive integers):", version2)