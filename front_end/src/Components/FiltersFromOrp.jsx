const FiltersFromOrp = () => (
  <div id="filters-container" className="govuk-!-padding-top-6 govuk-!-padding-left-2">
    <h2 className="govuk-heading-s">Apply filters</h2>
    <div className="filter-item govuk-!-padding-top-4 govuk-!-margin-bottom-0">
      <fieldset className="govuk-fieldset" data-module="display-selected">
        <legend className="govuk-fieldset__legend govuk-fieldset__legend--s">
          <h3 className="govuk-fieldset__heading">
            Publication date
          </h3>
        </legend>
        <p className="govuk-hint govuk-!-font-size-16">Not selected</p><details className="govuk-details govuk-!-margin-bottom-4" data-module="govuk-details">
          <summary className="govuk-details__summary" data-module="show-hide">Show</summary>
          <div className="govuk-form-group">
            <fieldset className="govuk-fieldset" role="group">
              <legend className="govuk-fieldset__legend govuk-fieldset__legend--s">
                <h3 className="govuk-fieldset__heading">From</h3>
              </legend>
              <div className="govuk-date-input" id="published-from">
                <div className="govuk-date-input__item">
                  <div className="govuk-form-group">
                    <label className="govuk-label govuk-date-input__label" for="published-from-day">
                      Day
                    </label>
                    <input className="govuk-input govuk-date-input__input govuk-input--width-2" id="published-from-day" name="publishedFrom-day" type="text" inputmode="numeric" value="" data-dashlane-rid="7fd59f4926a50b3e" data-dashlane-classification="date,day" />
                  </div>
                </div>
                <div className="govuk-date-input__item">
                  <div className="govuk-form-group">
                    <label className="govuk-label govuk-date-input__label" for="published-from-month">
                      Month
                    </label>
                    <input className="govuk-input govuk-date-input__input govuk-input--width-2" id="published-from-month" name="publishedFrom-month" type="text" inputmode="numeric" value="" data-dashlane-rid="85c75b818a219c7e" data-dashlane-classification="date,month" />
                  </div>
                </div>
                <div className="govuk-date-input__item">
                  <div className="govuk-form-group">
                    <label className="govuk-label govuk-date-input__label" for="published-from-year">
                      Year
                    </label>
                    <input className="govuk-input govuk-date-input__input govuk-input--width-4" id="published-from-year" name="publishedFrom-year" type="text" inputmode="numeric" value="" data-dashlane-rid="115beed9b74bec7e" data-dashlane-classification="date,year" />
                  </div>
                </div>
              </div>
            </fieldset>
          </div>
          <div className="govuk-form-group">
            <fieldset className="govuk-fieldset" role="group">
              <legend className="govuk-fieldset__legend govuk-fieldset__legend--s">
                <h3 className="govuk-fieldset__heading">To</h3>
              </legend>
              <div className="govuk-date-input" id="published-to">
                <div className="govuk-date-input__item">
                  <div className="govuk-form-group">
                    <label className="govuk-label govuk-date-input__label" for="published-to-day">
                      Day
                    </label>
                    <input className="govuk-input govuk-date-input__input govuk-input--width-2" id="published-to-day" name="publishedTo-day" type="text" inputmode="numeric" value="" data-dashlane-rid="9da2e28c2ad07c87" data-dashlane-classification="date,day" />
                  </div>
                </div>
                <div className="govuk-date-input__item">
                  <div className="govuk-form-group">
                    <label className="govuk-label govuk-date-input__label" for="published-to-month">
                      Month
                    </label>
                    <input className="govuk-input govuk-date-input__input govuk-input--width-2" id="published-to-month" name="publishedTo-month" type="text" inputmode="numeric" value="" data-dashlane-rid="4b48c96b298a2519" data-dashlane-classification="date,month" />
                  </div>
                </div>
                <div className="govuk-date-input__item">
                  <div className="govuk-form-group">
                    <label className="govuk-label govuk-date-input__label" for="published-to-year">
                      Year
                    </label>
                    <input className="govuk-input govuk-date-input__input govuk-input--width-4" id="published-to-year" name="publishedTo-year" type="text" inputmode="numeric" value="" data-dashlane-rid="4c32471519593101" data-dashlane-classification="date,year" />
                  </div>
                </div>
              </div>
            </fieldset>
          </div>
        </details>
      </fieldset>
    </div>


    <div className="govuk-form-group filter-item govuk-!-padding-top-4 govuk-!-margin-bottom-0">
      <fieldset className="govuk-fieldset" data-module="count-checked">
        <legend className="govuk-fieldset__legend govuk-fieldset__legend--s">
          <h3 className="govuk-fieldset__heading">
            Regulator
          </h3>
        </legend>
        <p className="govuk-hint govuk-!-font-size-16">0 selected</p><details className="govuk-details govuk-!-margin-bottom-4" data-module="govuk-details">
          <summary className="govuk-details__summary" data-module="show-hide">Show</summary>
          <div className="govuk-checkboxes" data-module="govuk-checkboxes">


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-ukas" name="regulators" type="checkbox" value="ukas" data-dashlane-rid="34bb7930f6bae068" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-ukas">
                Accreditation Service
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-asa" name="regulators" type="checkbox" value="asa" data-dashlane-rid="a12f1635f3bc19c4" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-asa">
                Advertising Standards Authority
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-bsb" name="regulators" type="checkbox" value="bsb" data-dashlane-rid="cf0ad6af256a8532" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-bsb">
                Bar Standards Board
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-bbfc" name="regulators" type="checkbox" value="bbfc" data-dashlane-rid="614212a43c3c3c9d" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-bbfc">
                British Board of Film Classification
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-cqc" name="regulators" type="checkbox" value="cqc" data-dashlane-rid="f628045685054e18" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-cqc">
                Care Quality Commission
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-ccew" name="regulators" type="checkbox" value="ccew" data-dashlane-rid="feb5c810ea5e67a1" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-ccew">
                Charity Commission for England and Wales
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-cimspa" name="regulators" type="checkbox" value="cimspa" data-dashlane-rid="44b5454e24692eaf" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-cimspa">
                Chartered Institute for the Management of Sport and Physical Activity
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-cilex" name="regulators" type="checkbox" value="cilex" data-dashlane-rid="8bd3e31bc2703b45" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-cilex">
                Chartered Institute of Legal Executives
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-caa" name="regulators" type="checkbox" value="caa" data-dashlane-rid="5eff8e5e4122b8b3" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-caa">
                Civil Aviation Authority
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-cma" name="regulators" type="checkbox" value="cma" data-dashlane-rid="08128aa1393fef18" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-cma">
                Competition and Markets Authority
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-cnhc" name="regulators" type="checkbox" value="cnhc" data-dashlane-rid="a1fd24f21a8d4b63" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-cnhc">
                Complementary and Natural Healthcare Council
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-clc" name="regulators" type="checkbox" value="clc" data-dashlane-rid="9815cba3ea81309e" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-clc">
                Council for Licensed Conveyancers
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-corgi" name="regulators" type="checkbox" value="corgi" data-dashlane-rid="b1f891be715c7fa9" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-corgi">
                Council for Registered Gas Installers
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-engc" name="regulators" type="checkbox" value="engc" data-dashlane-rid="8b87121efdc7f78b" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-engc">
                Engineering Council
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-ea" name="regulators" type="checkbox" value="ea" data-dashlane-rid="906c0c8a7b302d43" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-ea">
                Environment Agency
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-ehrc" name="regulators" type="checkbox" value="ehrc" data-dashlane-rid="508f2f66797770c6" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-ehrc">
                Equality and Human Rights Commission
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-fca" name="regulators" type="checkbox" value="fca" data-dashlane-rid="997e10a7009826a7" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-fca">
                Financial Conduct Authority
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-frc" name="regulators" type="checkbox" value="frc" data-dashlane-rid="a904307d640e1126" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-frc">
                Financial Reporting Council
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-fsa" name="regulators" type="checkbox" value="fsa" data-dashlane-rid="448c8b81d1e6f7ef" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-fsa">
                Food Standards Agency
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-fsr" name="regulators" type="checkbox" value="fsr" data-dashlane-rid="332736e664438a0a" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-fsr">
                Forensic Science Regulator
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-fr" name="regulators" type="checkbox" value="fr" data-dashlane-rid="6f7eaa1a332c8f65" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-fr">
                Fundraising Regulator
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-gc" name="regulators" type="checkbox" value="gc" data-dashlane-rid="6eda4b9f6c464582" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-gc">
                Gambling Commission
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-glaa" name="regulators" type="checkbox" value="glaa" data-dashlane-rid="94bf0617edf6c8a0" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-glaa">
                Gangmasters and Labour Abuse Authority
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-gcc" name="regulators" type="checkbox" value="gcc" data-dashlane-rid="f8cba574bb42def5" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-gcc">
                General Chiropractic Council
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-gdc" name="regulators" type="checkbox" value="gdc" data-dashlane-rid="faacc6d6f417f5d1" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-gdc">
                General Dental Council
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-gmc" name="regulators" type="checkbox" value="gmc" data-dashlane-rid="ec16098796b9fb97" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-gmc">
                General Medical Council
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-goc" name="regulators" type="checkbox" value="goc" data-dashlane-rid="e6525f82cd0017b9" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-goc">
                General Optical Council
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-gosc" name="regulators" type="checkbox" value="gosc" data-dashlane-rid="5ae4c5844719aced" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-gosc">
                General Osteopathic Council
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-gphc" name="regulators" type="checkbox" value="gphc" data-dashlane-rid="4efb65ba53526350" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-gphc">
                General Pharmaceutical Council
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-hcpc" name="regulators" type="checkbox" value="hcpc" data-dashlane-rid="16d99c21a37ed367" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-hcpc">
                Health and Care Professions Council
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-hse" name="regulators" type="checkbox" value="hse" data-dashlane-rid="60889f16eebbbd07" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-hse">
                Health and Safety Executive
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-hsib" name="regulators" type="checkbox" value="hsib" data-dashlane-rid="75a45e8cd3667a1a" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-hsib">
                Healthcare Safety Investigation Branch
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-hfea" name="regulators" type="checkbox" value="hfea" data-dashlane-rid="3d34554f96df45b6" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-hfea">
                Human Fertilisation and Embryology Authority
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-hta" name="regulators" type="checkbox" value="hta" data-dashlane-rid="920f57949a23c440" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-hta">
                Human Tissue Authority
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-impress" name="regulators" type="checkbox" value="impress" data-dashlane-rid="5694196bb9ea8f57" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-impress">
                Independent Monitor for the Press
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-iopc" name="regulators" type="checkbox" value="iopc" data-dashlane-rid="c513124a0cc5c4ad" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-iopc">
                Independent Office for Police Conduct
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-ipso" name="regulators" type="checkbox" value="ipso" data-dashlane-rid="301862a456ed2779" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-ipso">
                Independent Press Standards Organisation
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-ico" name="regulators" type="checkbox" value="ico" data-dashlane-rid="06e55b22d2bbd2b7" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-ico">
                Information Commissioner's Office
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-icaew" name="regulators" type="checkbox" value="icaew" data-dashlane-rid="4246cb818049b8ba" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-icaew">
                Institute of Chartered Accountants in England and Wales
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-mmo" name="regulators" type="checkbox" value="mmo" data-dashlane-rid="6cbe467e0102b451" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-mmo">
                Marine Management Organisation
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-mof" name="regulators" type="checkbox" value="mof" data-dashlane-rid="ad7949e24158e523" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-mof">
                Master of the Faculties
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-mhra" name="regulators" type="checkbox" value="mhra" data-dashlane-rid="57d8ca938d2a9058" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-mhra">
                Medicines and Healthcare products Regulatory Agency
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-nsta" name="regulators" type="checkbox" value="nsta" data-dashlane-rid="48087c4b21a515cc" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-nsta">
                North Sea Transition Authority
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-nmc" name="regulators" type="checkbox" value="nmc" data-dashlane-rid="497c99585ea2f47d" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-nmc">
                Nursing and Midwifery Council
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-onr" name="regulators" type="checkbox" value="onr" data-dashlane-rid="472df0ec0fa9fd3c" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-onr">
                Office for Nuclear Regulation
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-ofsted" name="regulators" type="checkbox" value="ofsted" data-dashlane-rid="b74bb4d627106b13" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-ofsted">
                Office for Standards in Education, Children's Services &amp; Skills
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-ofs" name="regulators" type="checkbox" value="ofs" data-dashlane-rid="fe3374b3e9f2c1ed" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-ofs">
                Office for Students
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-ofcom" name="regulators" type="checkbox" value="ofcom" data-dashlane-rid="20b28d1fbe31e722" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-ofcom">
                Office of Communications
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-ofgem" name="regulators" type="checkbox" value="ofgem" data-dashlane-rid="cff2e851bd69434d" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-ofgem">
                Office of Gas and Electricity Markets
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-ofqual" name="regulators" type="checkbox" value="ofqual" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-ofqual">
                Office of Qualifications and Examinations Regulation
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-orr" name="regulators" type="checkbox" value="orr" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-orr">
                Office of Rail and Road
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-oisc" name="regulators" type="checkbox" value="oisc" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-oisc">
                Office of the Immigration Services Commissioner
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-orcic" name="regulators" type="checkbox" value="orcic" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-orcic">
                Office of the Regulator of Community Interest Companies
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-psr" name="regulators" type="checkbox" value="psr" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-psr">
                Payment Systems Regulator
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-tpr" name="regulators" type="checkbox" value="tpr" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-tpr">
                Pensions Regulator
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-pins" name="regulators" type="checkbox" value="pins" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-pins">
                Planning Inspectorate
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-psa" name="regulators" type="checkbox" value="psa" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-psa">
                Professional Standards Authority for Health and Social Care
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-pra" name="regulators" type="checkbox" value="pra" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-pra">
                Prudential Regulation Authority
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-rsh" name="regulators" type="checkbox" value="rsh" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-rsh">
                Regulator of Social Housing
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-sia" name="regulators" type="checkbox" value="sia" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-sia">
                Security Industry Authority
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-swe" name="regulators" type="checkbox" value="swe" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-swe">
                Social Work England
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-sra" name="regulators" type="checkbox" value="sra" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-sra">
                Solicitors Regulation Authority
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-dmc" name="regulators" type="checkbox" value="dmc" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-dmc">
                The Data and Marketing Commission
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-opbas" name="regulators" type="checkbox" value="opbas" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-opbas">
                The Office for Professional Body Anti-Money Laundering Supervision
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-ofwat" name="regulators" type="checkbox" value="ofwat" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-ofwat">
                Water Services Regulation Authority
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="regulator-Safety" name="regulators" type="checkbox" value="Safety" />
              <label className="govuk-label govuk-checkboxes__label" for="regulator-Safety">
                Safety Tech Accelerator
              </label>
            </div>

          </div>
        </details>
      </fieldset>
    </div>


    <div className="govuk-form-group filter-item govuk-!-padding-top-4 govuk-!-margin-bottom-0">
      <fieldset className="govuk-fieldset" data-module="count-checked">
        <legend className="govuk-fieldset__legend govuk-fieldset__legend--s">
          <h3 className="govuk-fieldset__heading">
            Document Type
          </h3>
        </legend>
        <p className="govuk-hint govuk-!-font-size-16">0 selected</p><details className="govuk-details govuk-!-margin-bottom-4" data-module="govuk-details">
          <summary className="govuk-details__summary" data-module="show-hide">Show</summary>
          <div className="govuk-checkboxes" data-module="govuk-checkboxes">


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="docType-GD" name="docTypes" type="checkbox" value="GD" data-dashlane-rid="330bfa5d2c12979b" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="docType-GD">
                Guidance
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="docType-MSI" name="docTypes" type="checkbox" value="MSI" data-dashlane-rid="3a4e1f447fad45ca" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="docType-MSI">
                Market data, Standards and Information
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="docType-HS" name="docTypes" type="checkbox" value="HS" data-dashlane-rid="0936d518ab01ba72" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="docType-HS">
                Horizon Scanning
              </label>
            </div>

          </div>
        </details>
      </fieldset>
    </div>


    <div className="govuk-form-group filter-item govuk-!-padding-top-4 govuk-!-margin-bottom-0">
      <fieldset className="govuk-fieldset" data-module="count-selections">
        <legend className="govuk-fieldset__legend govuk-fieldset__legend--s">
          <h3 className="govuk-fieldset__heading">
            Topics
          </h3>
        </legend>
        <p className="govuk-hint govuk-!-font-size-16">0 selected</p><details className="govuk-details govuk-!-margin-bottom-4" data-module="govuk-details">
          <summary className="govuk-details__summary" data-module="show-hide">Show</summary>
          <div className="govuk-checkboxes" data-module="govuk-checkboxes">

            <div className="govuk-form-group">
              <label className="govuk-label" for="topic1">
                Primary Topic
              </label>
              <select className="govuk-select" id="topic1" name="topic1" data-module="topic-sub-selects">
                <option value="all">All</option>

                <option value="/entering-staying-uk">
                  Entering and staying in the UK
                </option>

                <option value="/going-and-being-abroad">
                  Going and being abroad
                </option>

                <option value="/education">
                  Education, training and skills
                </option>

                <option value="/childcare-parenting">
                  Parenting, childcare and children's services
                </option>

                <option value="/corporate-information">
                  Corporate information
                </option>

                <option value="/transport">
                  Transport
                </option>

                <option value="/environment">
                  Environment
                </option>

                <option value="/welfare">
                  Welfare
                </option>

                <option value="/housing-local-and-community">
                  Housing, local and community
                </option>

                <option value="/life-circumstances">
                  Life circumstances
                </option>

                <option value="/international">
                  International
                </option>

                <option value="/defence-and-armed-forces">
                  Defence and armed forces
                </option>

                <option value="/crime-justice-and-law">
                  Crime, justice and law
                </option>

                <option value="/regional-and-local-government">
                  Regional and local government
                </option>

                <option value="/society-and-culture">
                  Society and culture
                </option>

                <option value="/government">
                  Government
                </option>

                <option value="/work">
                  Work
                </option>

                <option value="/money">
                  Money
                </option>

                <option value="/business-and-industry">
                  Business and industry
                </option>

                <option value="/health-and-social-care">
                  Health and social care
                </option>

                <option value="/brexit">
                  Brexit
                </option>

                <option value="/coronavirus-taxon">
                  Coronavirus (COVID-19)
                </option>

              </select>
            </div><div className="govuk-form-group">  <label className="govuk-label" for="topic2">    Secondary Topic  </label>  <select className="govuk-select govuk-!-width-full" id="select-topic2" name="topic2" data-dashlane-rid="3f76cea881c5e26f" data-dashlane-classification="other"><option value="all" selected="selected">All</option></select></div>
          </div>
        </details>
      </fieldset>
    </div>


    <div className="govuk-form-group filter-item govuk-!-padding-top-4 govuk-!-margin-bottom-0">
      <fieldset className="govuk-fieldset" data-module="count-checked">
        <legend className="govuk-fieldset__legend govuk-fieldset__legend--s">
          <h3 className="govuk-fieldset__heading">
            Status
          </h3>
        </legend>
        <p className="govuk-hint govuk-!-font-size-16">1 selected</p><details className="govuk-details govuk-!-margin-bottom-4" data-module="govuk-details">
          <summary className="govuk-details__summary" data-module="show-hide">Show</summary>
          <div className="govuk-checkboxes" data-module="govuk-checkboxes">


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="status-active" name="status" type="checkbox" value="active" data-dashlane-rid="c5b093745813b5d7" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="status-active">
                Active
              </label>
            </div>


            <div className="govuk-checkboxes__item govuk-checkboxes--small">
              <input className="govuk-checkboxes__input" id="status-draft" name="status" type="checkbox" value="draft" checked="" data-dashlane-rid="cbc6755c764a4e74" data-dashlane-classification="other" />
              <label className="govuk-label govuk-checkboxes__label" for="status-draft">
                Draft
              </label>
            </div>

          </div>
        </details>
      </fieldset>
    </div>
  </div>
)

export { FiltersFromOrp }