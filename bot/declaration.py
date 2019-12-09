countries = [
            {'key':136, 'text':'Русия'},
            {'key':171, 'text':'Украйна'},
            {'key':111, 'text':'Молдова'},
            {'key':16, 'text':'Беларус'},
            {'key':71, 'text':'Казахстан'}
            ]

educations = [
            {'key':5, 'text':'Без образование'},
            {'key':1, 'text':'Начално'},
            {'key':2, 'text':'Средно'},
            {'key':3, 'text':'Висше'},
            {'key':4, 'text':'Основно'}
            ]

docFields = {
    'email':{'text':'E-mail', 'required': True},
    'name':{'text':'Име', 'required': True},
    'middleName':{'text':'Презиме', 'required': True},
    'surname':{'text':'Фамилия', 'required': True},
    'directionToIds':{'text':'Да послужи пред', 'required': True, 
        'multiple': True,
        'values': [
            {'key':1, 'text':'Министерство на правосъдието'},
            {'key':2, 'text':'Министерство на образованието, младежта и науката'},
            {'key':3, 'text':'СДВР - постоянно'},
            {'key':4, 'text':'СДВР - продължително'}
            ]
        } ,
    'countryId':{'text':'Роден в (държава)', 'required': True, 
        'values': countries
        },
    'region':{'text':'Роден в (регион)', 'required': True},
    'dateOfBirth':{'text':'Дата на раждане (ГГГГ-ММ-ДД)', 'required': True},
    'actOfBirth':{'text':'Акт на раждане', 'required': True},
    'citizenship':{'text':'Гражданство', 'required': True, 
        'values': countries
    },
    'otherCitizenships':{'text':'Други гражданства', 'required': False},
    'educationLevelId':{'text':'Образование', 'required': True,
        'values': educations
        },
    'speciality':{'text':'Специалност', 'required': False},
    'graduationDatePlace':{'text':'Кога и къде сте завършили?', 'required': False},
    'nationality':{'text':'Произход', 'required': False},
    'citizenshipAddress':{'text':'Постоянен адрес', 'required': False},
    'phone':{'text':'Телефон', 'required': False},
    'profession':{'text':'Професия', 'required': False},
    'isMilitaryServed':{'text':'Отбили ли сте наборна военна служба', 'required': False,
        'values': [
            {'key':1, 'text':'Да'},
            {'key':0, 'text':'Не'}
            ]
        },
    'motherName':{'text':'Майка: Име', 'required': True},
    'motherMiddleName':{'text':'Майка: Презиме', 'required': True},
    'motherSurname':{'text':'Майка: Фамилия', 'required': True},
    'motherDateOfBirth':{'text':'Майка: Дата на раждане (ГГГГ-ММ-ДД)', 'required': False},
    'motherPlaceOfBirth':{'text':'Майка: Място на раждане', 'required': False},
    'motherEducationLeveld':{'text':'Майка: Образование', 'required': False,
        'values': educations
    },
    'motherWork':{'text':'Майка: Месторабота', 'required': False},
    'motherNationality':{'text':'Майка: Произход', 'required': False},
    'motherCitizenship':{'text':'Майка: Гражданство', 'required': False,
        'values': countries
    },
    'motherOtherCitizenships':{'text':'Майка: Други гражданства', 'required': False},
    'fatherName':{'text':'Баща: Име', 'required': True},
    'fatherMiddleName':{'text':'Баща: Презиме', 'required': True},
    'fatherSurname':{'text':'Баща: Фамилия', 'required': True},
    'fatherDateOfBirth':{'text':'Баща: Дата на раждане: (ГГГГ-ММ-ДД)', 'required': False},
    'fatherPlaceOfBirth':{'text':'Баща: Място на раждане', 'required': False},
    'fatherEducationLeveld':{'text':'Баща: Образование', 'required': False,
        'values': educations
    },
    'fatherWork':{'text':'Баща: Месторабота', 'required': False},
    'fatherNationality':{'text':'Баща: Произход', 'required': False},
    'fatherCitizenship':{'text':'Баща: Гражданство', 'required': False,
        'values': countries
    },
    'fatherOtherCitizenships':{'text':'Баща: Други гражданства', 'required': False},
    'mateName':{'text':'Съпруг/а: Име', 'required': False},
    'mateMiddleName':{'text':'Съпруг/а: Презиме', 'required': False},
    'mateSurname':{'text':'Съпруг/а: Фамилия', 'required': False},
    'mateDateOfBirth':{'text':'Съпруг/а: Дата на раждане: (ГГГГ-ММ-ДД)', 'required': False},
    'matePlaceOfBirth':{'text':'Съпруг/а: Място на раждане', 'required': False},
    'mateEducationLeveld':{'text':'Съпруг/а: Образование', 'required': False,
        'values': educations
    },    
    'mateWork':{'text':'Съпруг/а: Месторабота', 'required': False},
    'mateNationality':{'text':'Съпруг/а: Произход', 'required': False},
    'mateCitizenship':{'text':'Съпруг/а: Гражданство', 'required': False,
        'values': countries
    },
    'mateOtherCitizenships':{'text':'Съпруг/а: Други гражданства', 'required': False},
    'brothersAndSistersInfo':{'text':'Братя и сестри', 'required': False},
    'childrenInfo':{'text':'Деца', 'required': False},
    'bulgarianLivingRelativesInfo':{'text':'Имате ли роднини, живеещи в Република България?', 'required': False},
    'bulgarianRelativesInfo':{'text':'Имате ли роднини, които са български граждани или които са били български граждани?', 'required': False},
    'livingInBulgariaInfo':{'text':'Смятате ли да се установите трайно в Република България, кога и къде? ', 'required': False}
}

dtFields = {
    'from': {'key': 'date_from', 'text': 'начальную желаемую дату приема в формате "ГГГГ-ММ-ДД"', 'required': True},
    'to': {'key': 'date_to', 'text': 'конечную желаемую дату приема в формате "ГГГГ-ММ-ДД"', 'required': True},
}

requestFields = {
    'dt': dtFields,
    'doc': docFields
}


def getField(name):
    field = dtFields.get(name) or docFields.get(name)
    return field


def getNextUnfilledValue(res, dictionary):
    for key in dictionary:
        if res.get(key) is None:
            return res, key
    return res, None


def getRequestItem(name, request):
    doc = request.get('doc',{}) or {}
    dt = request.get('dt',{}) or {}
    if name in dt.keys():
        return dt, name
    if name in doc.keys():
        return doc, name
    return None, None


def checkDeclaration(user):
        step = None
        request = user.get('request', {})
        doc = request.get('doc',{}) 
        dt = request.get('dt',{}) 
        dt, step = getNextUnfilledValue(dt, dtFields)
        if step is None:
                doc, step = getNextUnfilledValue(doc, docFields)
        request = {
                'doc': doc,
                'dt': dt
        }
        return request, step