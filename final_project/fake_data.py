import argparse
import pandas as pd
import numpy as np
import uuid
from datetime import datetime, timedelta
import os

def generate_patients(num_patients):
    """
    Generate a DataFrame of patients with unique IDs, emails, registration dates, and customer segments.
    """
    patient_ids = [str(uuid.uuid4()) for _ in range(num_patients)]
    first_names = [f'FirstName{idx}' for idx in range(num_patients)]
    last_names = [f'LastName{idx}' for idx in range(num_patients)]
    start_date = datetime.now() - timedelta(days=365*100)
    dates_of_birth = [start_date + timedelta(days=np.random.randint(0, 365*100)) for _ in range(num_patients)]
    genders = np.random.choice(['Male', 'Female'], size=num_patients)
    addresses = [f'Address {idx}' for idx in range(num_patients)]
    phone_numbers = [f'123-456-789{idx % 10}' for idx in range(num_patients)]
    emails = [f'patient{idx}@example.com' for idx in range(num_patients)]

    patients = pd.DataFrame({
        'patient_id': patient_ids,
        'first_name': first_names,
        'last_name': last_names,
        'date_of_birth': dates_of_birth,
        'gender': genders,
        'address': addresses,
        'phone_number': phone_numbers,
        'email': emails
    })
    return patients

def generate_appointments(num_appointments, patient_ids, doctor_ids):
    """
    Generate a DataFrame of appointments with unique IDs, associated patient IDs, doctor IDs, appointment dates, times, and statuses.
    """
    appointment_ids = [str(uuid.uuid4()) for _ in range(num_appointments)]
    patient_id_choices = np.random.choice(patient_ids, size=num_appointments)
    doctor_id_choices = np.random.choice(doctor_ids, size=num_appointments)
    start_date = datetime.now() - timedelta(days=365*5)
    appointment_dates = [start_date + timedelta(days=np.random.randint(0, 365*5)) for _ in range(num_appointments)]
    appointment_times = [datetime.now().time() for _ in range(num_appointments)]
    appointment_statuses = np.random.choice(['Scheduled', 'Completed', 'Cancelled'], size=num_appointments)

    appointments = pd.DataFrame({
        'appointment_id': appointment_ids,
        'patient_id': patient_id_choices,
        'doctor_id': doctor_id_choices,
        'appointment_date': appointment_dates,
        'appointment_time': appointment_times,
        'appointment_status': appointment_statuses
    })
    return appointments

def generate_doctors(num_doctors):
    doctor_ids = [str(uuid.uuid4()) for _ in range(num_doctors)]
    first_names = [f'DoctorFirstName{idx}' for idx in range(num_doctors)]
    last_names = [f'DoctorLastName{idx}' for idx in range(num_doctors)]
    specializations = np.random.choice(['Cardiology', 'Neurology', 'Orthopedics', 'Pediatrics'], size=num_doctors)
    phone_numbers = [f'987-654-321{idx % 10}' for idx in range(num_doctors)]
    emails = [f'doctor{idx}@example.com' for idx in range(num_doctors)]
    clinic_addresses = [f'Clinic Address {idx}' for idx in range(num_doctors)]

    doctors = pd.DataFrame({
        'doctor_id': doctor_ids,
        'first_name': first_names,
        'last_name': last_names,
        'specialization': specializations,
        'phone_number': phone_numbers,
        'email': emails,
        'clinic_address': clinic_addresses
    })
    return doctors

def generate_medical_records(num_records, patient_ids, doctor_ids):
    """
    Generate a DataFrame of medical records with unique IDs, associated patient IDs, doctor IDs, visit dates, diagnoses, treatments, prescriptions, and notes.
    """
    record_ids = [str(uuid.uuid4()) for _ in range(num_records)]
    patient_id_choices = np.random.choice(patient_ids, size=num_records)
    doctor_id_choices = np.random.choice(doctor_ids, size=num_records)
    start_date = datetime.now() - timedelta(days=365*5)
    visit_dates = [start_date + timedelta(days=np.random.randint(0, 365*5)) for _ in range(num_records)]
    diagnoses = [f'Diagnosis {idx}' for idx in range(num_records)]
    treatments = [f'Treatment {idx}' for idx in range(num_records)]
    prescriptions = [f'Prescription {idx}' for idx in range(num_records)]
    notes = [f'Notes {idx}' for idx in range(num_records)]

    medical_records = pd.DataFrame({
        'record_id': record_ids,
        'patient_id': patient_id_choices,
        'doctor_id': doctor_id_choices,
        'visit_date': visit_dates,
        'diagnosis': diagnoses,
        'treatment': treatments,
        'prescription': prescriptions,
        'notes': notes
    })
    return medical_records

def generate_prescriptions(num_prescriptions, patient_ids, doctor_ids):
    """
    Generate a DataFrame of prescriptions with unique IDs, associated patient IDs, doctor IDs, medication names, dosages, frequencies, start and end dates.
    """
    prescription_ids = [str(uuid.uuid4()) for _ in range(num_prescriptions)]
    patient_id_choices = np.random.choice(patient_ids, size=num_prescriptions)
    doctor_id_choices = np.random.choice(doctor_ids, size=num_prescriptions)
    medication_names = [f'Medication {idx}' for idx in range(num_prescriptions)]
    dosages = [f'{np.random.randint(1, 100)}mg' for _ in range(num_prescriptions)]
    frequencies = [f'{np.random.randint(1, 4)} times a day' for _ in range(num_prescriptions)]
    start_date = datetime.now() - timedelta(days=365*5)
    start_dates = [start_date + timedelta(days=np.random.randint(0, 365*5)) for _ in range(num_prescriptions)]
    end_dates = [start + timedelta(days=30) for start in start_dates]

    prescriptions = pd.DataFrame({
        'prescription_id': prescription_ids,
        'patient_id': patient_id_choices,
        'doctor_id': doctor_id_choices,
        'medication_name': medication_names,
        'dosage': dosages,
        'frequency': frequencies,
        'start_date': start_dates,
        'end_date': end_dates
    })
    return prescriptions

def generate_billing(num_bills, patient_ids, appointment_ids):
    """
    Generate a DataFrame of billing records with unique IDs, associated patient IDs, appointment IDs, amounts, billing dates, and payment statuses.
    """
    billing_ids = [str(uuid.uuid4()) for _ in range(num_bills)]
    patient_id_choices = np.random.choice(patient_ids, size=num_bills)
    appointment_id_choices = np.random.choice(appointment_ids, size=num_bills)
    amounts = np.round(np.random.uniform(50, 1000, size=num_bills), 2)
    start_date = datetime.now() - timedelta(days=365*5)
    billing_dates = [start_date + timedelta(days=np.random.randint(0, 365*5)) for _ in range(num_bills)]
    payment_statuses = np.random.choice(['Paid', 'Pending', 'Overdue'], size=num_bills)

    billing = pd.DataFrame({
        'billing_id': billing_ids,
        'patient_id': patient_id_choices,
        'appointment_id': appointment_id_choices,
        'amount': amounts,
        'billing_date': billing_dates,
        'payment_status': payment_statuses
    })
    return billing

def generate_insurance(num_insurances, patient_ids):
    """
    Generate a DataFrame of insurance records with unique IDs, associated patient IDs, insurance providers, policy numbers, coverage start and end dates.
    """
    insurance_ids = [str(uuid.uuid4()) for _ in range(num_insurances)]
    patient_id_choices = np.random.choice(patient_ids, size=num_insurances)
    insurance_providers = [f'Provider {idx}' for idx in range(num_insurances)]
    policy_numbers = [f'Policy{idx}' for idx in range(num_insurances)]
    start_date = datetime.now() - timedelta(days=365*5)
    coverage_start_dates = [start_date + timedelta(days=np.random.randint(0, 365*5)) for _ in range(num_insurances)]
    coverage_end_dates = [start + timedelta(days=365) for start in coverage_start_dates]

    insurance = pd.DataFrame({
        'insurance_id': insurance_ids,
        'patient_id': patient_id_choices,
        'insurance_provider': insurance_providers,
        'policy_number': policy_numbers,
        'coverage_start_date': coverage_start_dates,
        'coverage_end_date': coverage_end_dates
    })
    return insurance

def generate_lab_results(num_results, patient_ids):
    """
    Generate a DataFrame of lab results with unique IDs, associated patient IDs, test names, test dates, result values, normal ranges, and units.
    """
    lab_result_ids = [str(uuid.uuid4()) for _ in range(num_results)]
    patient_id_choices = np.random.choice(patient_ids, size=num_results)
    test_names = [f'Test {idx}' for idx in range(num_results)]
    start_date = datetime.now() - timedelta(days=365*5)
    test_dates = [start_date + timedelta(days=np.random.randint(0, 365*5)) for _ in range(num_results)]
    result_values = np.round(np.random.uniform(0, 100, size=num_results), 2)
    normal_ranges = ['0-100'] * num_results
    units = ['mg/dL'] * num_results

    lab_results = pd.DataFrame({
        'lab_result_id': lab_result_ids,
        'patient_id': patient_id_choices,
        'test_name': test_names,
        'test_date': test_dates,
        'result_value': result_values,
        'normal_range': normal_ranges,
        'units': units
    })
    return lab_results

def generate_medications(num_medications):
    medication_ids = [str(uuid.uuid4()) for _ in range(num_medications)]
    medication_names = [f'Medication {idx}' for idx in range(num_medications)]
    descriptions = [f'Description {idx}' for idx in range(num_medications)]
    side_effects = [f'Side effects {idx}' for idx in range(num_medications)]
    contraindications = [f'Contraindications {idx}' for idx in range(num_medications)]
    dosage_forms = np.random.choice(['Tablet', 'Capsule', 'Liquid'], size=num_medications)

    medications = pd.DataFrame({
        'medication_id': medication_ids,
        'medication_name': medication_names,
        'description': descriptions,
        'side_effects': side_effects,
        'contraindications': contraindications,
        'dosage_form': dosage_forms
    })
    return medications

def generate_facilities(num_facilities):
    facility_ids = [str(uuid.uuid4()) for _ in range(num_facilities)]
    facility_names = [f'Facility {idx}' for idx in range(num_facilities)]
    addresses = [f'Address {idx}' for idx in range(num_facilities)]
    phone_numbers = [f'555-123-456{idx % 10}' for idx in range(num_facilities)]
    emails = [f'facility{idx}@example.com' for idx in range(num_facilities)]
    facility_types = np.random.choice(['Hospital', 'Clinic', 'Pharmacy'], size=num_facilities)

    facilities = pd.DataFrame({
        'facility_id': facility_ids,
        'facility_name': facility_names,
        'address': addresses,
        'phone_number': phone_numbers,
        'email': emails,
        'facility_type': facility_types
    })
    return facilities

def adjust_counts(desired_size_bytes, counts):
    """
    Adjust the counts of each dataset to achieve the desired total size in bytes.
    """
    estimated_total_size = sum([count * size for count, size in counts.values()])
    scaling_factor = desired_size_bytes / estimated_total_size
    for key in counts:
        count, size = counts[key]
        counts[key] = (int(count * scaling_factor), size)
    return counts

def main(desired_size_bytes=1e9):
    num_patients = 10000
    num_doctors = 1000
    num_appointments = 50000
    num_records = 50000
    num_prescriptions = 20000
    num_bills = 20000
    num_insurances = 10000
    num_lab_results = 30000
    num_medications = 1000
    num_facilities = 500

    counts = {
        'patients': (num_patients, 500),
        'doctors': (num_doctors, 500),
        'appointments': (num_appointments, 300),
        'medical_records': (num_records, 400),
        'prescriptions': (num_prescriptions, 300),
        'billing': (num_bills, 200),
        'insurance': (num_insurances, 200),
        'lab_results': (num_lab_results, 300),
        'medications': (num_medications, 200),
        'facilities': (num_facilities, 300)
    }

    counts = adjust_counts(desired_size_bytes, counts)

    patients = generate_patients(counts['patients'][0])
    doctors = generate_doctors(counts['doctors'][0])
    appointments = generate_appointments(counts['appointments'][0], patients['patient_id'], doctors['doctor_id'])
    medical_records = generate_medical_records(counts['medical_records'][0], patients['patient_id'], doctors['doctor_id'])
    prescriptions = generate_prescriptions(counts['prescriptions'][0], patients['patient_id'], doctors['doctor_id'])
    billing = generate_billing(counts['billing'][0], patients['patient_id'], appointments['appointment_id'])
    insurance = generate_insurance(counts['insurance'][0], patients['patient_id'])
    lab_results = generate_lab_results(counts['lab_results'][0], patients['patient_id'])
    medications = generate_medications(counts['medications'][0])
    facilities = generate_facilities(counts['facilities'][0])

    os.makedirs('data', exist_ok=True)
    patients.to_csv('data/patients.csv', index=False)
    doctors.to_csv('data/doctors.csv', index=False)
    appointments.to_csv('data/appointments.csv', index=False)
    medical_records.to_csv('data/medical_records.csv', index=False)
    prescriptions.to_csv('data/prescriptions.csv', index=False)
    billing.to_csv('data/billing.csv', index=False)
    insurance.to_csv('data/insurance.csv', index=False)
    lab_results.to_csv('data/lab_results.csv', index=False)
    medications.to_csv('data/medications.csv', index=False)
    facilities.to_csv('data/facilities.csv', index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate healthcare datasets.')
    parser.add_argument('--size', type=float, default=1e9, help='Desired total size of the datasets in bytes (default: 1GB)')
    args = parser.parse_args()
    main(args.size)