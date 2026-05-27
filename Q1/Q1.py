import math

slots = 72
pole_pairs = 3
phases = 3
layers = 2

# slots per pole per phase
q = slots / (2 * pole_pairs * phases)

# electrical slot angle in radians (alpha)
alpha = pole_pairs * 2 * math.pi / slots

# --- Distribution Factor Function ---
def calc_kd(n_harmonic):
    return math.sin(n_harmonic * q * alpha / 2) / (q * math.sin(n_harmonic * alpha / 2))

Kd1 = calc_kd(1)
Kd3 = calc_kd(3)
Kd5 = calc_kd(5)

# --- Pitch Factor Function ---
def calc_kp(n_harmonic, slots_spanned):
    # lambda is the electrical angle of the spanned slots
    lambda_rad = slots_spanned * alpha
    return math.sin(n_harmonic * lambda_rad / 2)

# Full Pitch (spans exactly 1 pole pitch = 12 slots)
Kfp1 = calc_kp(1, 12)
Kfp3 = calc_kp(3, 12)
Kfp5 = calc_kp(5, 12)

# Short Pitch 11/12 (spans 11 slots)
Ksp1 = calc_kp(1, 11)
Ksp3 = calc_kp(3, 11)
Ksp5 = calc_kp(5, 11)

# --- Winding Factor (Kw = Kd * Kp) ---
Kfw1, Kfw3, Kfw5 = Kd1 * Kfp1, Kd3 * Kfp3, Kd5 * Kfp5
Ksw1, Ksw3, Ksw5 = Kd1 * Ksp1, Kd3 * Ksp3, Kd5 * Ksp5

print(f"Full-Pitch Kw:  1st={Kfw1:.4f}, 3rd={Kfw3:.4f}, 5th={Kfw5:.4f}")
print(f"Short-Pitch Kw: 1st={Ksw1:.4f}, 3rd={Ksw3:.4f}, 5th={Ksw5:.4f}")
