""" First DB must be built"""
class CitizenHandler:
    
    def get_global_results():
        dummy_res = {
                "results": [
                    {
                        'illness': 'Covid',
                        'infected_count': 123,
                        'recovered_count': 50,
                        'deceased': 90,
                        're-infected': 2
                    },
                    {
                        'illness': 'Hepatitis',
                        'infected_count': 34234,
                        'recovered_count': 520,
                        'deceased': 90,
                        're-infected': 2
                    },
                    {
                        'illness': 'Influenza',
                        'infected_count': 10000,
                        'recovered_count': 0,
                        'deceased': 400,
                        're-infected': 2
                    }
                ]
            }
            
        return dummy_res

    def get_results_by_municapility(municipality, illness=None):
        if not illness:
            dummy_res = {
                "results": [
                    {
                        'illness': 'Covid',
                        'infected_count': 123,
                        'recovered_count': 50,
                        'deceased': 90,
                        're-infected': 2
                    },
                    {
                        'illness': 'Hepatitis',
                        'infected_count': 34234,
                        'recovered_count': 520,
                        'deceased': 90,
                        're-infected': 2
                    },
                    {
                        'illness': 'Influenza',
                        'infected_count': 10000,
                        'recovered_count': 0,
                        'deceased': 400,
                        're-infected': 2
                    }
                ]
            }
        else:
            dummy_res = {
                'illness': illness,
                'infected_count': 123,
                'recovered_count': 50,
                'deceased': 90,
                're-infected': 2
            }

        return dummy_res

    def get_results_by_sex(sex, illness=None):
        if not illness:
            dummy_res = {
                "results": [
                    {
                        'illness': 'Covid',
                        'infected_count': 123,
                        'recovered_count': 50,
                        'deceased': 90,
                        're-infected': 2
                    },
                    {
                        'illness': 'Hepatitis',
                        'infected_count': 34234,
                        'recovered_count': 520,
                        'deceased': 90,
                        're-infected': 2
                    },
                    {
                        'illness': 'Influenza',
                        'infected_count': 10000,
                        'recovered_count': 0,
                        'deceased': 400,
                        're-infected': 2
                    }
                ]
            }
        else:
            dummy_res = {
                'illness': illness,
                'infected_count': 123,
                'recovered_count': 50,
                'deceased': 90,
                're-infected': 2
            }

        return dummy_res

    def get_results_by_age(min_age, max_age, illness=None):
        if not illness:
            dummy_res = {
                "results": [
                    {
                        'illness': 'Covid',
                        'infected_count': 123,
                        'recovered_count': 50,
                        'deceased': 90,
                        're-infected': 2
                    },
                    {
                        'illness': 'Hepatitis',
                        'infected_count': 34234,
                        'recovered_count': 520,
                        'deceased': 90,
                        're-infected': 2
                    },
                    {
                        'illness': 'Influenza',
                        'infected_count': 10000,
                        'recovered_count': 0,
                        'deceased': 400,
                        're-infected': 2
                    }
                ]
            }
        else:
            dummy_res = {
                'illness': illness,
                'infected_count': 123,
                'recovered_count': 50,
                'deceased': 90,
                're-infected': 2
            }

        return dummy_res