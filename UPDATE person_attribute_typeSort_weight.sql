UPDATE
    person_attribute_type
SET
    sort_weight = CASE
        WHEN name = 'Phone Number' THEN 1
        WHEN name = 'Alternative Phone Number' THEN 2
        WHEN name = 'Primary Contact person''s Name' THEN 3
        WHEN name = 'Primary Contact Phone Number' THEN 4
        WHEN name = 'primaryRelative' THEN 5
        WHEN name = 'education' THEN 6
        WHEN name = 'occupation' THEN 7
        WHEN name = 'Occupational Status' THEN 8
        WHEN name = 'Marital Status' THEN 9
        WHEN name = 'email' THEN 10
        WHEN name = 'PaymentMethod' THEN 10
        WHEN name = 'PaymentDetails' THEN 11
        WHEN name = 'FreePaymentDetails' THEN 12
        WHEN name = 'Sponsor' THEN 13
        WHEN name = 'Reference Number' THEN 14
        WHEN name = 'ReferredFrom' THEN 15
        WHEN name = 'medicolegalcases' THEN 16
        WHEN name = 'Is Emergency' THEN 17
        WHEN name = 'credit companies' THEN 18
        WHEN name = 'CBHI agreed woredas' THEN 19
        WHEN name = 'familyNameLocal' THEN 20
        WHEN name = 'middleNameLocal' THEN 21
        WHEN name = 'caste' THEN 22
        WHEN name = 'class' THEN 23
        WHEN name = 'primaryContact' THEN 24
        WHEN name = 'secondaryContact' THEN 25
        WHEN name = 'secondaryIdentifier' THEN 26
        WHEN name = 'landHolding' THEN 27
        WHEN name = 'debt' THEN 28
        WHEN name = 'distanceFromCenter' THEN 29
        WHEN name = 'isUrban' THEN 30
        WHEN name = 'cluster' THEN 31
        WHEN name = 'RationCard' THEN 32
        WHEN name = 'familyIncome' THEN 33
        WHEN name = 'Originofreferral' THEN 35
        WHEN name = 'InsuranceName' THEN 36
    END
WHERE
    name IN (
        'Phone Number',
        'Alternative Phone Number',
        'Primary Contact person''s Name',
        'Primary Contact Phone Number',
        'primaryRelative',
        'education',
        'occupation',
        'Occupational Status',
        'Marital Status',
        'PaymentMethod',
        'PaymentDetails',
        'FreePaymentDetails',
        'Reference Number',
        'Sponsor',
        'ReferredFrom',
        'medicolegalcases',
        'Is Emergency',
        'credit companies',
        'CBHI agreed woredas',
        'familyNameLocal',
        'middleNameLocal',
        'caste',
        'class',
        'primaryContact',
        'secondaryContact',
        'secondaryIdentifier',
        'landHolding',
        'debt',
        'distanceFromCenter',
        'isUrban',
        'cluster',
        'RationCard',
        'familyIncome',
        'email',
        'Originofreferral',
        'InsuranceName'
    );